#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 15:51:48 2020

@author: aishit
"""


import pandas as pd
from config import Config

def Gen_Latex():
    config = Config()
    
    # AWARDS ACHIEVEMENTS -------------------------------------------
    # a_a_data = pd.read_csv('a_a_data.csv')
    a_a_data = pd.read_excel('../resume_data_1page.xlsx', sheet_name='a_a_data')
    awards_achievements_template_head = r"""\begin{itemize}[itemsep = -0.75mm, leftmargin=*]"""
    awards_achievements_template_head = awards_achievements_template_head.replace('-0.75mm', config.a_a_itemsep)
    awards_achievements_template_foot = r"""\end{itemize}"""
    
    a_as = []
    df = a_a_data
    project = awards_achievements_template_head
    for n_a in range(len(df)):
        project = project + '\n \item {' + str(df['a_a'][n_a]) + '} \n'
    project = project + awards_achievements_template_foot
    
    file = open("temp/a_a.txt","w")
    file.writelines(project)
    file.close()
    
    # WORK EXP ----------------------------------------------------
    we_data = pd.read_excel('../resume_data_1page.xlsx', sheet_name='we_data')
    project_template = r"""\begin{itemize}[label={}, leftmargin=0cm, itemsep = -1mm]
        \item \textbf{{company_name}} | \emph{position}\hfill \emph{date}
        \vspace*{-2mm}
        \begin{itemize}[itemsep = -0.4 mm, leftmargin=*, label=\tiny$\bullet$]
            \item {}
            \vspace*{-0.5mm}
            \item {}
            \vspace*{-0.5mm}
            \item {}
            \item {}
        \end{itemize}
    \end{itemize}
    """
    project_template = project_template.replace('itemsep = -1mm]', ('itemsep = ' + config.project_itemsep_1 + ']'))
    project_template = project_template.replace('itemsep = -0.4 mm', ('itemsep = ' + config.project_itemsep_2))
    project_template = project_template.replace('vspace*{-2mm', ('vspace*{' + config.project_vspace_1))
    if config.inter_point_vspace_bool==1:
    	project_template = project_template.replace('vspace*{-0.5mm', ('vspace*{' + config.inter_point_vspace))
    else:
    	project_template = project_template.replace('vspace*{-0.5mm}', '')
    
    projects = []
    df = we_data
    for n_proj in range(len(df)):
        project = project_template.replace('project_name', df['project'][n_proj])
        project = project.replace('company_name', df['company'][n_proj])
        project = project.replace('position', df['position'][n_proj])
        project = project.replace('date', df['date'][n_proj])
        for i in range(1,5):
            col_name = 'item_'+str(i)
            if pd.notnull(df[col_name][n_proj]):
                project = project.replace('item {', ('item{'+df[col_name][n_proj]), 1)
            else:
                project = project.replace('\item {}', '', 1)
        if n_proj!=len(df)-1:
            project += r'\vspace*{' + config.project_vspace_2 + r"""}
    """
        
        project = project.replace(r'\vspace*{-0.6mm', ('\vspace*{' + config.project_vspace_3))
        projects.append(project)
        
    file = open("temp/wes.txt","w")
    for proj in projects:
        file.writelines(proj)
    file.close()
    
    
    # PROJECTS ----------------------------------------------------
    project_data = pd.read_excel('../resume_data_1page.xlsx', sheet_name='project_data')
    project_template = r"""\begin{itemize}[label={}, leftmargin=0cm, itemsep = -1mm]
        \item \textbf{{project_name}} | {position} \hfill \emph{date}
        \vspace*{-2mm}
        \begin{itemize}[itemsep = -0.4 mm, leftmargin=*, label=\tiny$\bullet$]
            \item {}
            \vspace*{-0.5mm}
            \item {}
            \item {}
            \item {}
        \end{itemize}
    \end{itemize}
    """
    project_template = project_template.replace('itemsep = -1mm]', ('itemsep = ' + config.project_itemsep_1 + ']'))
    project_template = project_template.replace('itemsep = -0.4 mm', ('itemsep = ' + config.project_itemsep_2))
    project_template = project_template.replace('vspace*{-2mm', ('vspace*{' + config.project_vspace_1))
    if config.inter_point_vspace_bool==1:
    	project_template = project_template.replace('vspace*{-0.5mm', ('vspace*{' + config.inter_point_vspace))
    else:
    	project_template = project_template.replace('vspace*{-0.5mm}', '')
    
    projects = []
    df = project_data
    for n_proj in range(len(df)):
        project = project_template.replace('project_name', df['project'][n_proj])
        if config.inter_point_vspace_bool==1 and df['project'][n_proj]==r'Mark 47$^{\#}$':
        	project = project.replace(('vspace*{'+str(config.inter_point_vspace)), ('vspace*{' + config.inter_point_vspace_mark_47))
        project = project.replace('company_name', df['company'][n_proj])
        project = project.replace('position', df['position'][n_proj])
        project = project.replace('date', df['date'][n_proj])

        for i in range(1,5):
            col_name = 'item_'+str(i)
            if pd.notnull(df[col_name][n_proj]):
                project = project.replace('item {', ('item{'+df[col_name][n_proj]), 1)
            else:
                project = project.replace('\item {}', '', 1)
                
        if n_proj!=len(df)-1:
            project += r'\vspace*{' + config.project_vspace_2 + r"""}
    """
        project = project.replace(r"""}
                                  \item {""", r"""}
                                  \vspace*{-0.6mm}
                                  \item {""", 1)
        project = project.replace(r'\vspace*{-0.6mm', ('\vspace*{' + config.project_vspace_3))
        projects.append(project)
        
    file = open("temp/projects.txt","w")
    for proj in projects:
        file.writelines(proj)
    file.close()
    
    # POR --------------------------------------------------
    # por_data = pd.read_csv('por_data.csv')
    por_data = pd.read_excel('../resume_data_1page.xlsx', sheet_name='por_data')
    por_template = r"""\begin{itemize}[label={}, leftmargin=0cm, itemsep = -1mm]
        \item \textbf{{por}} {pordept} \hfill \emph{{date}}\vspace*{-2mm}
        \begin{itemize}[itemsep = -0.4 mm, leftmargin=*, label=\tiny$\bullet$]
            \item {}
            \vspace*{-0.5mm}
            \item {}
            \item {}
            \item {}
        \end{itemize}
    \end{itemize}
    """
    por_template = por_template.replace('itemsep = -1mm]', ('itemsep = ' + config.por_itemsep_1 + ']'))
    por_template = por_template.replace('itemsep = -0.4 mm', ('itemsep = ' + config.por_itemsep_2))
    por_template = por_template.replace('vspace*{-2mm', ('vspace*{' + config.por_vspace_1))
    if config.inter_point_vspace_bool==1:
    	por_template = por_template.replace('vspace*{-0.5mm', ('vspace*{' + config.inter_point_vspace))
    else:
    	por_template = por_template.replace('vspace*{-0.5mm}', '')
    
    pors = []
    df = por_data
    for n_por in range(len(df)):
        project = por_template.replace('por', df['por'][n_por], 1)
        if pd.notnull(df['pordept'][n_por]):
        	project = project.replace('pordept', df['pordept'][n_por], 1)
        else:
        	project = project.replace('pordept', '')
        project = project.replace('date', df['date'][n_por])
        for i in range(1,5):
            col_name = 'item_'+str(i)
            if pd.notnull(df[col_name][n_por]):
                project = project.replace('item {', ('item{'+df[col_name][n_por]), 1)
            else:
                project = project.replace('\item {}', '', 1)
        if n_por!=len(df)-1:
            project += r'\vspace*{' + config.por_vspace_2 + r"""}
    """
        project = project.replace(r"""}
                                  \item {""", r"""}
                                  \vspace*{-0.6mm}
                                  \item {""", 1)
        project = project.replace(r'\vspace*{-0.6mm', ('\vspace*{' + config.project_vspace_3))
        pors.append(project)
        
    file = open("temp/pors.txt","w")
    for por in pors:
        file.writelines(por)
    file.close()
    
    # TECHNICAL PROFICIENCY
    tp_data = pd.read_excel('../resume_data_1page.xlsx', sheet_name='tp_data')
    tp_template_head = r"""\begin{itemize}[itemsep = -0.75mm, leftmargin=*]"""
    tp_template_foot = r"""\end{itemize}"""
    
    tp_template_head = tp_template_head.replace('itemsep = -0.75mm', ('itemsep = ' + config.tp_itemsep))
    
    tps = []
    df = tp_data
    project = tp_template_head
    for n_tp in range(len(df)):
        project = project + '\n \item {' + str(df['tp'][n_tp]) + '} \n'
    project = project + tp_template_foot
    
    file = open("temp/tps.txt","w")
    file.writelines(project)
    file.close()
    
    # KEY COURSES UNDERTAKEN
    kcu_data = pd.read_excel('../resume_data_1page.xlsx', sheet_name='kcu_data')
    # kcu_template_head = r"""\begin{itemize}[itemsep = -0.75mm, leftmargin=*]"""
    # kcu_template_foot = r"""\end{itemize}"""
    kcu_template_head = tp_template_head
    kcu_template_foot = tp_template_foot
    kcus = []
    df = kcu_data
    project = kcu_template_head
    for n_tp in range(len(df)):
        project = project + '\n \item {' + str(df['kcu'][n_tp]) + '} \n'
    project = project + kcu_template_foot
    
    file = open("temp/kcus.txt","w")
    file.writelines(project)
    file.close()
    
    # EXTRACURRICULARS
    ec_data = pd.read_excel('../resume_data_1page.xlsx', sheet_name='ec_data')
    ec_template = r"""\begin{itemize}[itemsep = -0.75 mm, leftmargin=*]
                \item {}
                \item {}
                \item {}
                \item {}
                \item {}
		\end{itemize}
    """
    
    ec_template = ec_template.replace('itemsep = -0.75 mm', ('itemsep = ' + config.ec_itemsep_1))
    # ec_template = ec_template.replace('vspace*{-2mm', ('vspace*{' + config.ec_vspace_1))
    
    ecs = []
    df = ec_data
    project = ec_template
    for n_ec in range(len(df)):
        for i in range(1,6):
            col_name = 'item_'+str(i)
            if pd.notnull(df[col_name][n_ec]):
                project = project.replace('item {', ('item{'+df[col_name][n_ec]), 1)
            else:
                project = project.replace('\item {}', '', 1)
    ecs.append(project)
        
    file = open("temp/ecs.txt","w")
    for ec in ecs:
        file.writelines(ec)
    file.close()