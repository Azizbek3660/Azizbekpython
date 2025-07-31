import pandas as pd
import numpy as np
sales_data=pd.read_csv('sales_data.csv')
sales_data
sales_data.groupby("Category").agg(
    total_quantity=pd.NamedAgg(column="Quantity",aggfunc="sum"),
    avg_price=pd.NamedAgg(column="Price",aggfunc="mean"), 
    max_quantity=pd.NamedAgg(column="Quantity",aggfunc="max"),
)
sales_data.groupby("Category").agg(    max_quantity=pd.NamedAgg(column="Quantity",aggfunc="max"))
import pandas as pd
from io import StringIO
import pandas as pd
from io import StringIO

# CSV ma'lumotlarini ko‘chirish
data = """Date,Product,Category,Quantity,Price
2023-01-01,Laptop,Electronics,10,800
2023-01-01,T-Shirt,Clothing,5,20
2023-01-02,Smartphone,Electronics,8,400
2023-01-02,Coffee Maker,Home,12,50
2023-01-03,Jeans,Clothing,15,30
2023-01-03,Blender,Home,6,60
2023-01-04,Headphones,Electronics,10,150
2023-01-04,Sweater,Clothing,7,35
2023-01-05,Toaster,Home,8,25
2023-01-05,Tablet,Electronics,12,300
2023-01-06,Sneakers,Clothing,10,50
2023-01-06,Vacuum Cleaner,Home,5,80
2023-01-07,Smart TV,Electronics,15,1000
2023-01-07,Hoodie,Clothing,6,25
2023-01-08,Blu-ray Player,Home,9,70
2023-01-08,Wireless Earbuds,Electronics,11,120
2023-01-09,Denim Jacket,Clothing,13,45
2023-01-09,Air Purifier,Home,7,90
2023-01-10,Gaming Console,Electronics,14,400
2023-01-10,Formal Shirt,Clothing,8,35
2023-01-11,Cookware Set,Home,10,60
2023-01-11,External Hard Drive,Electronics,9,80
2023-01-12,Sunglasses,Clothing,11,15
2023-01-12,Desk Lamp,Home,6,25
2023-01-13,Wireless Speaker,Electronics,12,70
2023-01-13,Sweatpants,Clothing,7,20
2023-01-14,Coffee Table,Home,8,100
2023-01-14,Drone,Electronics,10,300
2023-01-15,Backpack,Clothing,14,40
2023-01-15,Comforter Set,Home,7,45
2023-01-16,Fitness Tracker,Electronics,9,60
2023-01-16,Casual Shoes,Clothing,6,30
2023-01-17,Kitchen Scale,Home,12,20
2023-01-17,Projector,Electronics,13,200
2023-01-18,Dress Shirt,Clothing,8,25
2023-01-18,Steam Iron,Home,11,30
2023-01-19,Soundbar,Electronics,15,150
2023-01-19,Sweatshirt,Clothing,7,35
2023-01-20,Bedside Lamp,Home,10,20
2023-01-20,Point-and-Shoot Camera,Electronics,8,250
2023-01-21,Sport Shoes,Clothing,12,40
2023-01-21,Desk Chair,Home,6,75
2023-01-22,Wireless Mouse,Electronics,11,25
2023-01-22,Summer Dress,Clothing,9,30
2023-01-23,Pressure Cooker,Home,14,50
2023-01-23,Bluetooth Headset,Electronics,7,50
2023-01-24,Denim Skirt,Clothing,8,25
2023-01-24,Bookshelf,Home,13,80
2023-01-25,4K Monitor,Electronics,9,350
2023-01-25,Cargo Pants,Clothing,11,30"""

# Ma'lumotlarni o'qish
df = pd.read_csv(StringIO(data))

# Har bir qatordagi umumiy savdo = Quantity × Price
df['TotalSales'] = df['Quantity'] * df['Price']

# Sana bo‘yicha umumiy savdoni hisoblash
sales_by_date = df.groupby('Date')['TotalSales'].sum()

# Eng ko‘p savdo bo‘lgan sanani topish
max_sales_date = sales_by_date.idxmax()
max_sales_amount = sales_by_date.max()

# Natijani chiqarish
print("📅 Eng ko‘p savdo qilingan sana:", max_sales_date)
print("💰 Umumiy savdo miqdori:", max_sales_amount)

Homework Assignment 2: Examining Customer Orders
cus_orders=pd.read_csv("customer_orders.csv")
🔧 1. Kutubxonalarni yuklash
python
Копировать
Редактировать
import pandas as pd
import sqlite3
📥 2. Ma’lumotlarni o‘qish
🔹 SQLite'dan population jadvalini o‘qiymiz:
python
Копировать
Редактировать
# SQLite bazani ochish
conn = sqlite3.connect("task/population.db")

# 'population' jadvalidan ma’lumotlar
population_df = pd.read_sql_query("SELECT * FROM population", conn)

# Bog‘lanishni yopamiz
conn.close()
🔹 Excel'dan Salary Band ma’lumotlari:
python
Копировать
Редактировать
salary_band_df = pd.read_excel("task/population salary analysis.xlsx")
🔍 3. Salary Band belgilash
Qo‘l bilan har bir salary uchun to‘g‘ri band topamiz:
python
Копировать
Редактировать
def get_salary_band(salary):
    for _, row in salary_band_df.iterrows():
        min_salary = row['MinSalary']
        max_salary = row['MaxSalary']
        if pd.isna(max_salary):
            if salary >= min_salary:
                return row['Band']
        elif min_salary <= salary <= max_salary:
            return row['Band']
    return 'Unknown'

population_df['SalaryBand'] = population_df['Salary'].apply(get_salary_band)
📊 4. Tahlillar:
python
Копировать
Редактировать
# 1. Band bo‘yicha aholi soni
count_per_band = population_df['SalaryBand'].value_counts().rename("PopulationCount")

# 2. Band bo‘yicha o‘rtacha oylik
avg_salary = population_df.groupby('SalaryBand')['Salary'].mean().rename("AverageSalary")

# 3. Band bo‘yicha median oylik
median_salary = population_df.groupby('SalaryBand')['Salary'].median().rename("MedianSalary")

# 4. Band bo‘yicha foiz
total_population = len(population_df)
percent_per_band = (count_per_band / total_population * 100).rename("PopulationPercentage")
🧾 5. Final Jadval:
python
Копировать
Редактировать
# Barchasini birlashtiramiz
final_df = pd.concat([count_per_band, percent_per_band, avg_salary, median_salary], axis=1)

# Foiz formatini yaxshilash
final_df['PopulationPercentage'] = final_df['PopulationPercentage'].round(2)

print(final_df.reset_index().rename(columns={'index': 'SalaryBand'}))
✅ Natija:
Siz quyidagicha jadval olasiz:

SalaryBand	PopulationCount	PopulationPercentage	AverageSalary	MedianSalary
Low	...	... %	...	...
Medium	...	... %	...	...
High	...	... %	...	...
Very High	...	... %	...	...
