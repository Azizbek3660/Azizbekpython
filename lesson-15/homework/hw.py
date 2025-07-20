1.Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field.
import pyodbc
import pyodbc

# 1. Yangi bazani yaratamiz (MyCrewDB)
master_connection = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-A3B6K6V;'
    'DATABASE=master;'
    'Trusted_Connection=yes;'
)
master_cursor = master_connection.cursor()
master_cursor.execute("IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'MyCrewDB') CREATE DATABASE MyCrewDB")
master_connection.commit()
master_cursor.close()
master_connection.close()

# 2. MyCrewDB bazasiga ulanamiz
connection = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-A3B6K6V;'
    'DATABASE=MyCrewDB;'
    'Trusted_Connection=yes;'
)
cursor = connection.cursor()

# 3. Jadval yaratish (Roster)
create_table_query = """
IF NOT EXISTS (
    SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Roster'
)
CREATE TABLE Roster (
    Name VARCHAR(50),
    Species VARCHAR(50),
    Age INT
)
"""
cursor.execute(create_table_query)

# 4. Ma’lumot qo‘shish
insert_query = """
INSERT INTO Roster (Name, Species, Age)
VALUES
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
"""
cursor.execute(insert_query)
connection.commit()

# 5. Ismni yangilash: Jadzia Dax → Ezri Dax
update_query = """
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
"""
cursor.execute(update_query)
connection.commit()

# 6. Species = 'Bajoran' bo‘lganlarning Name va Age ni chiqarish
select_query = """
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran'
"""
cursor.execute(select_query)
rows = cursor.fetchall()

print("Species = 'Bajoran' bo‘lganlar:")
for row in rows:
    print(f"Name: {row.Name}, Age: {row.Age}")

# 7. Yopish
cursor.close()
connection.close()
