import os
import openai
import pdb

def main():
    openai.api_key = "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"
    company = input('Company: ')
    position = input('Position: ')
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"Write me a cover letter for {position} with {company}.\n\nNicholas Demetrick\n\nEducation\n\n-Bachelors of science in pure mathematics\n- Univesity Of British Columbia\n- Complete courses in machine learning, continuous optimization and time series analysis.\n\nAbout me \n\n- Quick learner\n- Great at communications \n- Passionate about problem solving\n\nSkill \n\n- Vim\n- SQL \n- Linux\n- Python \n-R\n-Java \n-Latex\n\nProjects\n\n- Reddit web scraper that pulled and categorized 50,000 images.\n\n-Encrypted chat app made completely from base python library and uses military grade 2048 bit RSA encryption.\n\n- Terrorism analytics based on 180,000 different attacks, focusing on country, method and organization.  \n",
      temperature=0.7,
      max_tokens=2542,
      top_p=1,
      best_of=5,
      frequency_penalty=0,
      presence_penalty=0
    )
    print(response['choices'][0]['text']) 
    document = r'''
%!TEX TS-program = xelatex
%%%% Define Document type
\documentclass[11pt,a4]{article}

%%%% Include Packages
\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage{multicol}
\usepackage{hyperref}
\usepackage{csquotes}
\usepackage{tabularx}
\hypersetup{colorlinks=true,urlcolor=black}
\usepackage[11pt]{moresize}
\usepackage{setspace}
\usepackage{fontspec}
\usepackage[inline]{enumitem}
\usepackage{ragged2e}
\usepackage{anyfontsize}

%%%% Set Margins
\usepackage[margin=1cm]{geometry}

%%%% Set Fonts
\setmainfont[
BoldFont=SourceSansPro-Semibold.otf,
ItalicFont=SourceSansPro-RegularIt.otf
]{SourceSansPro-Regular.otf}

%%%% Set Page Style
\pagestyle{fancy}
\fancyhf{} 
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

%%%% Set URL Style
\urlstyle{same}



%%%% Set Indentation
\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

%%%% Set Secondary Color, Page Number Color, Footer Text
\definecolor{UI_blue}{RGB}{32, 64, 151}
\definecolor{HF_color}{RGB}{179, 179, 179}
\rfoot{{\color{HF_color} \thepage \ of \ 1, Updated \today}}

%%%% Set Heading Format
\titleformat{\section}{
	\color{UI_blue} \scshape \raggedright \large 
}{}{0em}{}[\vspace{-0.7cm} \hrulefill \vspace{-0.2cm}]
%%%%%%% --------------------------------------------------------------------------------------
%%%%%%% --------------------------------------------------------------------------------------
%%%%%%%  END OF "DO NOT TOUCH" REGION
%%%%%%% --------------------------------------------------------------------------------------
%%%%%%% --------------------------------------------------------------------------------------



\begin{document}
	%%%%%%% --------------------------------------------------------------------------------------
	%%%%%%%  HEADER
	%%%%%%% --------------------------------------------------------------------------------------
	\begin{center}
		
		\begin{minipage}[b]{0.5\textwidth}
			\centering
			{\Huge ''' + position + r'''} \\ %
			\vspace{0.1cm}
			%    {\color{UI_blue} \Large{Software Developer}} \\
			
		\end{minipage}% 
		
		\vspace{-0.15cm} 
		{\color{UI_blue} \hrulefill}
	\end{center}
	
	\justify
	\setlength{\parindent}{0pt}
	\setlength{\parskip}{12pt}
	\vspace{0.2cm}
	
	Date: \today \par \vspace{-0.1cm}'''  + response['choices'][0]['text'] + r''' \vspace{0.5cm} \raggedright \end{document}'''

    f = open("CoverLetter.tex", "w")
    f.write(document)
    f.close()   

    os.system("xelatex CoverLetter.tex")
    os.system('mv CoverLetter.pdf ~/Desktop')
if __name__ == '__main__':
    main()

