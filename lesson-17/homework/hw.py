Homework 1:

import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} df = pd.DataFrame(data)

1.Rename column names using function. "First Name" --> "first_name", "Age" --> "age
2.Print the first 3 rows of the DataFrame
3.Find the mean age of the individuals
4.Select and print only the 'Name' and 'City' columns
5.Add a new column 'Salary' with random salary values
6.Display summary statistics of the DataFrame
import pandas as pd
import numpy as np

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)
df
df=df.rename(columns={'First Name':'first_name'})
df=df.rename(columns={'Age':'age'})
df
df.head(3)
orta_yosh=df['age'].mean()
print ("orta_yosh:",orta_yosh)
df[["first_name", "age"]]
df["Salary"]=np.random.randint(500,2000,size=len (df))
df
print(df.describe())
Homework 2:

1Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. Use below table.


Month	Sales	Expenses
Jan	5000	3000
Feb	6000	3500
Mar	7500	4000
Apr	8000	4500


1.Calculate and display the maximum sales and expenses.
2.Calculate and display the minimum sales and expenses.
3.Calculate and display the average sales and expenses.
data={
    "Month":['Jan','Feb','Mar','Apr'],
    "Sales":[5000,6000,7500,8000],
    "Expenses":[3000,3500,4000,4500]
}
sales_and_expenses=pd.DataFrame(data)
sales_and_expenses
max_sales=sales_and_expenses['Sales'].max()
max_expenses=sales_and_expenses['Expenses'].max()
print('max_sales:',max_sales)
print('max_expenses:',max_expenses)
min_sales=sales_and_expenses['Sales'].min()
min_expenses=sales_and_expenses['Expenses'].min()
print('min_sales:',min_sales)
print('min_expenses:',min_expenses)
average_sales=sales_and_expenses['Sales'].mean()
average_expenses=sales_and_expenses['Expenses'].mean()
print('avg_sales:',average_sales)
print('avg_expenses:',average_expenses)
1.Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.


Category	January	February	March	April
Rent	1200	1300	1400	1500
Utilities	200	220	240	250
Groceries	300	320	330	350
Entertainment	150	160	170	180


2.Calculate and display the maximum expense for each category.
3.Calculate and display the minimum expense for each category.
4.Calculate and display the average expense for each category.
import pandas as pd

expenses = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})
expenses = expenses.set_index('Category')
max_expenses = expenses.max(axis=1)
print('max_expenses')
print(max_expenses)
min_expenses = expenses.min(axis=1)
print('min_expenses')
print(min_expenses)
avg_expenses = expenses.mean(axis=1)
print('avg_expenses')
print(avg_expenses)
