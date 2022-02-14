Created on Fri Jan 14 15:14:51 2022



import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

IBM=pd.read_csv('/Users/nadimsaad/Desktop/IRONHACK/Module 2/Week 5/Day 25/IBM.csv')


st.title("IBM Employees")

def chart1(x):
    fig1, ax = plt.subplots()   
    ax.bar(arr, bins=20)
    plt.title('Total Employees by Department')
    plt.ylabel("Total Employees")
    st.pyplot(fig1)
    
def chart2(x):
    fig2, ax = plt.subplots()   
    ax.bar(arr, bins=20)
    plt.title('Monthly Income by Department')
    st.pyplot(fig2)

def chart3(x):
    fig3, ax = plt.subplots()   
    ax.bar(arr, bins=20)
    plt.title('Average Income by Department')
    st.pyplot(fig3)

def chart4(x): 
    fig4, ax = plt.subplots()   
    ax.pie(x, autopct='%1.1f%%',  
    startangle=90)
    plt.title('IBM Employees Job Satisfaction')
    st.pyplot(fig4)
    
add_selectbox1 = st.sidebar.selectbox("Choose your graph:",(
       "Total Employees by Department", "Monthly Income by Department", 
       "Average Income by Department", "IBM Employees Job Satisfaction"))

if add_selectbox1=="Total Employees by Department":
    chart1(IBM.groupby(by=['Department'])['MonthlyIncome'].sum())
    
elif add_selectbox1=="Monthly income by department":
    chart2(IBM.pivot_table(index=["Department"], values=['MonthlyIncome'],aggfunc=['sum','count']))

elif add_selectbox1=="Average Income by Department":
    chart3(IBM.groupby(by=['Department'])['MonthlyIncome'].mean())

elif add_selectbox1=="IBM Employees Job Satisfaction":
    chart4(IIBM.JobSatisfaction.value_counts())
    
def chart5(x):
    fig5, ax = plt.subplots()   
    ax.pie(x, autopct='%1.1f%%',  
    startangle=90, shadow=True, labels=['No', 'Yes'])
    plt.title('Percentage of Attrition')
    st.pyplot(fig5)
    
def chart6(x):
    fig6, ax = plt.subplots()   
    ax.boxplot()
    plt.title('Monthly Income per Attrition Type')
    st.pyplot(fig6)
        
def chart7(x):
    fig7, ax = plt.subplots()   
    ax.boxplot(column="YearsAtCompany",by="Attrition")
    plt.title('Attrition based on years at IBM')
    st.pyplot(fig7)

def chart8(x):
    fig8, ax = plt.subplots()   
    axs.set_xticklabels(axs.get_xticklabels(),rotation=45)
    axs.set_title('Attrition & Years at IBM per Department')
    st.pyplot(fig8)

def chart9(x):
    fig9, ax = plt.subplots()   
    ax.pie(x, autopct='%1.1f%%',  
    startangle=5, shadow=True, legend = False, fontsize=10)
    plt.title('Marital Satus of those who left IBM')
    st.pyplot(fig9)

add_selectbox2 = st.sidebar.selectbox("Choose your graph:",(
       "Percentage of Attrition", "Monthly income per Attrition Type", 
       "Attrition based on years at IBM", "Attrition & Years at IBM per Department",
       "Marital Satus of Employees who left IBM"))

if add_selectbox2=="Percentage of Attrition":
    chart5(IBM.Attrition.value_counts())

elif add_selectbox2=="Monthly income per Attrition Type":
    chart6(IBM.boxplot(column="MonthlyIncome",by="Attrition") )

elif add_selectbox2=="Attrition based on years at IBM":
    chart7(IBM.boxplot(column="YearsAtCompany",by="Attrition"))
    
elif add_selectbox2=="Attrition & Years at IBM per Department":
    chart8(IBM.boxplot(column="YearsAtCompany",by="Attrition"))
    
elif add_selectbox2=="Marital Satus of Employees who left IBM":
    chart9(sns.barplot(x="Department", y='YearsAtCompany', hue="Attrition", data=IBM)))

def chart10(x):
    fig10, ax = plt.subplots()   
    ax.bar(arr, bins=20)
    axs.set_title('Worklife Balance of Employees who left IBM')
    plt.xlabel("Satisfaction level")
    plt.ylabel("Number of employees")
    st.pyplot(fig10)

def chart11(x):
    fig11, ax = plt.subplots()   
    ax.bar(arr, bins=20)
    axs.set_title('Environment Satisfaction of Employees who left IBM')
    plt.xlabel("Satisfaction level")
    plt.ylabel("Number of employees")
    st.pyplot(fig11)
    
def chart12(x):
    fig12, ax = plt.subplots()   
    ax.bar(arr, bins=20)
    axs.set_title('Job Satisfaction of Employees who left IBM')
    plt.xlabel("Satisfaction level")
    plt.ylabel("Number of employees")
    st.pyplot(fig11)
    
add_selectbox3 = st.sidebar.selectbox("Choose your graph:",(
       "Worklife Balance of Employees who left IBM", 
       "Environment Satisfaction of Employees who left IBM",
       "Job Satisfaction of Employees who left IBM"))

mpg_labels = ['Bad', 'Good', 'Better', 'Best']

#Equal width bins: the range for each bin is the same size - we use pd.cut
bins = pd.cut(IBM['WorkLifeBalance'],4, labels=mpg_labels)

#New column 'bins1' with the labels as values
IBM['bins1'] = pd.cut(IBM['WorkLifeBalance'],4, labels=mpg_labels)
IBM.head(10)


#Environment Satisfaction: 
mpg_labels1 = ['Low', 'Medium', 'High', 'Very High']
               
#New column 'bins1' with the labels as values
IBM['bins2'] = pd.cut(IBM['EnvironmentSatisfaction'],4, labels=mpg_labels1)
IBM.head(10)             
               
#JobSatisfaction: 
mpg_labels2 =  ['Low', 'Medium', 'High', 'Very High']
IBM['bins3'] = pd.cut(IBM['JobSatisfaction'],4, labels=mpg_labels2)

if add_selectbox3=="Worklife Balance of Employees who left IBM":
    chart10(IBM['bins1'].value_counts()) )

elif add_selectbox3=="Environment Satisfaction of Employees who left IBM":
    chart11(IBM['bins2'].value_counts()"))

elif add_selectbox3=="Job Satisfaction of Employees who left IBM":
    chart12(IBM['bins3'].value_counts())
     
