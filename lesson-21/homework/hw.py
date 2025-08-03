Exercise 1: Calculate the average grade for each student.

Exercise 2: Find the student with the highest average grade.

Exercise 3: Create a new column 'Total' representing the total marks obtained by each student.

Exercise 4: Plot a bar chart to visualize the average grades in each subject.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

df1
df=df1[["Math","English","Science"]].mean(axis=1)
df
df1[["Math","English","Science"]].mean(axis=1).max()
df1["Tolat"]=df1[["Math","English","Science"]].sum(axis=1)
df1
plt.plot(df,marker='o',markersize=3,linestyle='dotted',linewidth = 2,label='Java',alpha=0.8)
Exercise 1: Calculate the total sales for each product.

Exercise 2: Find the date with the highest total sales.

Exercise 3: Calculate the percentage change in sales for each product from the previous day.

Exercise 4: Plot a line chart to visualize the sales trends for each product over time.
import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)
df2
df2["total"]=df2[["Product_A","Product_B","Product_C"]].sum(axis=1)
df2
max_day=df2[df2["total"]==df2["total"].max()]["Date"].values[0]
print("eng kop savdo:",max_day)
df2=df2.set_index("Date")

dd=df2.pct_change(1)
dd
plt.plot(dd,marker='o',markersize=3,linestyle='dotted',linewidth = 2,label='Java',alpha=0.8)
Exercise 1: Calculate the average salary for each department.

Exercise 2: Find the employee with the most experience.

Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary in the dataframe.

Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments.
import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

df3
df3.groupby("Department").agg({"Salary":"mean"})
df3["Experience (Years)"].max()
min_salary=df3["Salary"].min()
df3["Salary_increase"]=((df3["Salary"]-min_salary)/min_salary)*100
df3
plt.plot(min_salary,marker='o',markersize=3,linestyle='dotted',linewidth = 2,label='Java',alpha=0.8)
Exercise 1: Calculate the total revenue from all orders.

Exercise 2: Find the most ordered product.

Exercise 3: Calculate the average quantity of products ordered.

Exercise 4: Plot a pie chart to visualize the distribution of sales across different products.
import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)
df4
df4["Total_Price"].sum()
df4["Quantity"].max()
df4.groupby("Product").agg({"Quantity":"mean"})
sales_by_product = df4.groupby('Product')['Total_Price'].sum()
plt.figure(figsize=(6, 6))
sales_by_product.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Sales Distribution by Product')
plt.ylabel('')  # Yozuvni olib tashlash
plt.show()
