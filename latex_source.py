def return_doc(position, response):
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
    return document
