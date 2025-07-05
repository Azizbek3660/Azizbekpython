def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Nolga bo‘lish mumkin emas"
    return a / b


def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
geometry/
│
├── __init__.py
└── circle.py
📄 circle.py fayli:
python
Копировать код
import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius
math.pi – π (3.1415...) qiymatini beradi. Har ikki funksiya bitta argument – radius qabul qiladi.

📄 __init__.py fayli:
python
Копировать код
# Bo‘sh qoldirilsa ham bo‘ladi, ammo xohlasangiz circle funksiyalarini import qilsangiz bo‘ladi:

from .circle import calculate_area, calculate_circumference
📦 2. file_operations paketi
📁 Fayl tuzilmasi:
markdown
Копировать код
file_operations/
│
├── __init__.py
├── file_reader.py
└── file_writer.py
📄 file_reader.py fayli:
python
Копировать код
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Fayl topilmadi."
📄 file_writer.py fayli:
python
Копировать код
def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
📄 __init__.py fayli:
python
Копировать код
from .file_reader import read_file
from .file_writer import write_file
✅ Ularni ishlatish (main.py misol)
python
Копировать код
from geometry import calculate_area, calculate_circumference
from file_operations import read_file, write_file

# Geometry test
radius = 5
print("Doira yuzasi:", calculate_area(radius))
print("Aylana uzunligi:", calculate_circumference(radius))

# File test
file_path = "test.txt"
write_file(file_path, "Salom, bu test faylidir.")
print("Fayl mazmuni:", read_file(file_path))
