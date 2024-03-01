import os
import openai
import pdb
from prompt import get_prompt
from latex_source import return_doc
import sys

sys.path.append('/Users/work/Documents/Jobs/Cover')


def main():
    openai.api_key = "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"
    company = input('Company: ')
    position = input('Position: ')
    response = openai.Completion.create(
      model="gpt-3.5-turbo-instruct",
      prompt = get_prompt(company, position),
      temperature=0.7,
      max_tokens=2542,
      top_p=1,
      best_of=5,
      frequency_penalty=0,
      presence_penalty=0
    )

    document = return_doc(position, response)

    print(response['choices'][0]['text']) 
    f = open("CoverLetter.tex", "w")
    f.write(document)
    f.close()   

    os.system("xelatex CoverLetter.tex > /dev/null 2>&1")
    os.system('mv CoverLetter.pdf /Users/work/Documents/Jobs')
if __name__ == '__main__':
    main()

