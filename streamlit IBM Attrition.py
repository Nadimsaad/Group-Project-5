# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 22:47:59 2022

@author: Ingrid
"""

# Import librairies
#!pip install plotly==5.5.0
#pip install chart_studio
import chart_studio
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

import plotly.graph_objects as go
import seaborn as sns



# Load dataset
IBM=pd.read_csv('/Users/nadimsaad/Desktop/IRONHACK/Module 2/Week 5/Project 5/IBM.csv')


# Title of the dashboard
st.title("IBM - Human resources KPI📈")


# We want 5 colomns

Att_yes = IBM[(IBM['Attrition'] == 'Yes')]
Att_no = IBM[(IBM['Attrition'] == 'No')]
Total = Att_yes + Att_no

kpi1, kpi2, kpi3 , kpi4, kpi5, kpi6 = st.columns(6)
kpi1.metric(label = 'Number of employees' , value = len(Total))
kpi2.metric(label = 'Employees Attrition' , value = len(Att_yes))
kpi3.metric(label = 'IBM Employees' , value = len(Att_no))
kpi4.metric(label = 'Highest Salary $  ' , value= round( IBM['MonthlyIncome'].max()))
kpi5.metric(label = 'Average Salary $ ', value = round (IBM['MonthlyIncome'].mean()))
kpi6.metric(label = 'Lowest Salary $ ', value= round (IBM['MonthlyIncome'].min()))



# # We want2 colomns
# kpi7, kpi8 = st.columns(2)
# kpi7.metric(label = 'Minimum Salary', value=  IBM['MonthlyIncome'].min())
# kpi8.metric(label = 'Minimum Salary', value=  IBM['MonthlyIncome'].min())


    
    
# Install the widget on the side bar/ 1st selection
st.sidebar.title("Options :")
add_selectbox1 = st.sidebar.selectbox("Choose your table:",("Dataset", "Attrition",
    "Department", "Income", " Satisfaction"))

if add_selectbox1=="Dataset":
    st.write('Theme: List of IBM Employees')
    #st.write ('Shape : ', IBM.shape)
    st.write ('Describe : ', IBM.describe())
    if st.checkbox('Show/Hide data table'):
        st.write('The first 5 rows :', IBM.head(5) )
        

#if st.checkbox('Attrition in the company'):
if add_selectbox1 == 'Attrition':
    st.subheader ("Attrition Key Metrics")
    #Display 2 charts
    
    #Chart 1 - Bar chart
    
    fig1, ax = plt.subplots(figsize=(10,4))   
    
    ax = IBM['Attrition'].value_counts().plot(kind='bar',  color = ['dodgerblue', 'black'], edgecolor='black', fontsize = 8)
    ax.set_title('Employee Attrition in number', fontsize = 18)
    plt.xlabel("Attrition", fontsize =12)
    plt.ylabel("Number of employees", fontsize =12)
    st.pyplot(fig1)

    #Chart 2 - Pie Chart
    
    fig2, ax = plt.subplots(figsize=(10,4))  
    
    colors = ['dodgerblue', 'black']
    ax = IBM['Attrition'].value_counts().plot(kind='pie' , autopct='%1.1f%%', colors = colors, startangle=100, legend = True, labeldistance=1.15, wedgeprops = { 'linewidth' : 3, 'edgecolor' : 'white' }, fontsize=5)
    ax.set_title("Employee Attrition in percentage", fontsize = 7)
    plt.legend(fontsize=5) 
    ax.set_ylabel('') # remove the 'Attrition' foor axis 'Y'
    # ax.legend(loc=2, labels= ax.index)
    st.pyplot(fig2)
    
    
    
    # #Chart3 
    
    # Age = IBM['Age']
    # plt.hist(Age) 
    # st.pyplot(Age)


if add_selectbox1=="Department":
        
    #Chart 4 
    
    fig4, axs= plt.subplots(figsize=(10,4)) 
    
    axs = sns.barplot(x="Department", y='YearsAtCompany', hue="Attrition", data=IBM)
    axs.set_xticklabels(axs.get_xticklabels(),rotation=45)
    plt.suptitle('')
    axs.set_title('Attrition and Years in the company per department')
    plt.show()
    st.pyplot(fig4)
    


if add_selectbox1==" Satisfaction":
    st.subheader('Happiness')
    
   
    
   
    
   
if add_selectbox1=="Income":
    st.subheader("Monthly Income")
  
#     st.table(IBM.pivot_table(index=["Department"], values=['MonthlyIncome'],aggfunc=['sum','count']))

# # elif add_selectbox1=="Average Income by Department":
#     st.table(IBM.groupby(by=['Department'])['MonthlyIncome'].mean())

# elif add_selectbox1=="IBM Employees Job Satisfaction":
#     st.table(IBM.JobSatisfaction.value_counts())
    
#     fig3, ax = plt.subplots()
#     ax=IBM.JobSatisfaction.value_counts().plot(kind='pie', autopct='%1.1f%%', #format which work with non numeric value
# startangle=90, shadow=True, legend = True, fontsize=10)
#     ax.set_title("Job Satisfaction")
#     st.pyplot(fig3)
    







# 

#st.markdown('## Charts')   ## Main Title

#we want 2 charts
#df= data['JobSatisfaction']

#chart1, chart2 = st.columns(2)

#chart1.bar_chart(df)
#chart2.line_chart(df)

#we want to add the DF
#st.markdown('## Dataset')  ## Main Title
#st.dataframe(data)


    

#     #IBM.Attrition.value_counts().plot(kind='pie', autopct='%1.1f%%',startangle=90, shadow=True, labels=['No', 'Yes'], legend = True, fontsize=10)
#    # plt.title('Attrition in percentage')
#    # plt.show()

#     #IBM['Attrition'].value_counts().plot(kind='bar')
#     #plt.title('Attrition in number')
#     #plt.xlabel("Attrition")
#     #plt.ylabel("Number of employees")
#     #plt.show()




# #hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=4)

# #pie_chat = px.pie(df, values = 'Attrition', title = 'Attrition in percentage')

# IBM.Attrition.value_counts().plot(kind='pie', autopct='%1.1f%%', #format which work with non numeric value
# startangle=90, shadow=True, labels=['No', 'Yes'], legend = True, fontsize=10)
# plt.title('Attrition in percentage')
# plt.show()


