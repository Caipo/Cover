def get_prompt(company, position):
      prompt=f"Write me a cover letter for {position} with {company} that has no fill in the blanks.

Nicholas Demetrick

Education

-Bachelors of science in pure mathematics
- Univesity Of British Columbia
- Complete courses in machine learning, continuous optimization and time series analysis.

Experience
    
    AI intern at Super Geo AI 

    - Developed a Unet model with TensorFlow and a Yolov8 model to calculate wildlife damage caused by animals.
    - Assisted in researching AI models to predict changes in crop yields due to climate change.
    - Learned about different AI models and ML ops practices.

About me 

- Quick learner
- Great at communications 
- Passionate about problem solving

Skill 

- Vim
- SQL 
- Linux
- Python 
- R
- Java 
- Latex
- Docker
- Machine Learning

Projects

- Reddit web scraper that pulled and categorized 50,000 images.

-Encrypted chat app made completely from base python library and uses military grade 2048 bit RSA encryption.

- Terrorism analytics based on 180,000 different attacks, focusing on country, method and organization.  
"
      return prompt
