#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 17:49:54 2020

@author: aishit
"""


def Compile():
    head = r"""\documentclass[10.5pt]{article}
    \usepackage[a4paper,bottom = 0.6in,left = 0.75in,right = 0.75in,top = 0.6in]{geometry}
    \usepackage{graphicx}
    \usepackage{amsmath}
    \usepackage{array}
    \usepackage{enumitem}
    \usepackage{wrapfig}
    \usepackage{titlesec}
    \usepackage[colorlinks=false]{hyperref}
    \usepackage{verbatim}
    \usepackage{hyperref}
    \usepackage{xcolor}
    \usepackage{csquotes}
    \usepackage{microtype}
    \usepackage{textcomp}
    %\usepackage{lipsum}
    \usepackage[sfdefault]{ClearSans} %% option 'sfdefault' activates Clear Sans as the default text font
	\usepackage[T1]{fontenc}
    
    \newcommand{\xfilll}[2][1ex]{
    	\dimen0=#2\advance\dimen0 by #1
    	\leaders\hrule height \dimen0 depth -#1\hfill}
    \titleformat{\section}{\large\scshape\raggedright}{}{0em}{}
    \renewcommand\labelitemi{\raisebox{0.4ex}{\tiny$\bullet$}}
    \renewcommand{\labelitemii}{$\cdot$}
    \pagenumbering{gobble}
    \begin{document}
    	%\vspace*{3.5cm} one page
    	\vspace*{4.5cm}
    	\vspace*{-5pt}
    	
    	\begin{itemize}[leftmargin=*]
    		\item Pursuing a \textbf{Minor} degree in the department of \textbf{Computer Science and Engineering}
    	\end{itemize}
    	\vspace*{-0.8cm}
        """
    
    
    sections = [r'Awards \& Achievements', r'Work Experience', r'Key Projects', 
                r'Positions of Responsibility', r'Technical Proficiency',
                r'Key Courses Undertaken', r'Extra-Curriculars']
    
    section_template = r"""\section*{{\Large {section_name}}\xfilll[0pt]{0.5pt}}\vspace*{-0.3cm}
    """
    
    vspace = r"""\vspace*{-0.8cm}
    """
    
    parts = []
    f = open("temp/a_a.txt", "r")
    a_a = f.read()
    parts.append(a_a)
    
    f = open("temp/wes.txt", "r")
    projects = f.read()
    parts.append(projects)
    
    f = open("temp/projects.txt", "r")
    projects = f.read()
    parts.append(projects)
    
    f = open("temp/pors.txt", "r")
    pors = f.read()
    parts.append(pors)
    
    f = open("temp/tps.txt", "r")
    projects = f.read()
    parts.append(projects)
    
    f = open("temp/kcus.txt", "r")
    projects = f.read()
    parts.append(projects)
    
    f = open("temp/ecs.txt", "r")
    projects = f.read()
    parts.append(projects)
    
    full_text = head
    for part in range(len(parts)):
        section = section_template.replace('section_name', sections[part])
        full_text += section
        full_text += parts[part]
        full_text += vspace
    
    full_text += r"\end{document}"
        
    file = open("full_text.tex","w")
    file.writelines(full_text)
    file.close()