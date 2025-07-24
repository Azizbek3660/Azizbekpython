import pandas as pd
import numpy as np
df = pd.read_csv("tackoverflow_qa.csv")
df
1.Find all questions that were created before 2014
2.Find all questions with a score more than 50
3.Find all questions with a score between 50 and 100
4.Find all questions answered by Scott Boston
5.Find all questions answered by the following 5 users
6.Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.
7.Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
8.Find all questions that are not answered by Scott Boston
df['creationdate']=pd.to_datetime(df['creationdate'])
before_2014=df[df['creationdate']<'2014-01-01']
print(before_2014)
filt1=df['score']>50
df[filt1]
filt2=df['score'].between(50,100)
df[filt2]
filt3=df['ans_name']=='Scott Boston'
df[filt3]
filt4=df['answercount']==5
df[filt4]
df['creationdate']=pd.to_datetime(df['creationdate'])
march=df['creationdate'].dt.month>3
october=df['creationdate'].dt.month<10
filt5=df['ans_name']=='Unutbu'
filt6=df['score']<5
final = (march | october) & filt5 & filt6
df[final]
df
filt7=df['score'].between(5,10)
filt8=df['viewcount']>10000
final_filtr=filt7|filt8
df[final_filtr]

filt9=df['ans_name']!='Scott Boston'
df[filt9]
titanic_df = pd.read_csv("titanic.csv")
titanic_df
1.Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.
filt=titanic_df['Sex']=='female'
filt1=titanic_df['Age'].between(20,30)
filts=filt&filt1
titanic_df[filts]
Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.


new_filt1=titanic_df['Fare']>100
titanic_df[new_filt1]
Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).
new_filt2=titanic_df['Survived']==1
new_filt3=titanic_df['SibSp']==0
new_filt4=titanic_df['Parch']==0
all=new_filt2&new_filt3&new_filt4
titanic_df[all]

Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.
new_filt5=titanic_df['Embarked']=='C'
new_filt6=titanic_df['Fare']>50
fill=new_filt5&new_filt6
titanic_df[fill]
Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.
new_filt7=titanic_df['SibSp']>=1
new_filt8=titanic_df['Parch']>=1
all_f=new_filt7|new_filt8
titanic_df[all_f]

Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.
new_filt9=titanic_df['Survived']==0
new_filt10=titanic_df['Age'].between(0,15)
all_fil=new_filt9&new_filt10
titanic_df[all_fil]
Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.
new_filt11=titanic_df['Cabin'].notna()
new_filt12=titanic_df['Fare']>200
all_filt=new_filt11&new_filt12
titanic_df[all_filt]
Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.
new_filt13 = titanic_df['PassengerId'] % 2 == 1
titanic_df[new_filt13]
Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.
unique_ticket_passengers = df[~df['Ticket'].duplicated(keep=False)]
print(unique_ticket_passengers[['Name', 'Tiket']])
Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.
new_filt14=titanic_df['Name'].str.contains('Miss', case=False, na=False)
new_filt15=titanic_df['Pclass']==1
all_filts=new_filt14&new_filt15
titanic_df[all_filts]
