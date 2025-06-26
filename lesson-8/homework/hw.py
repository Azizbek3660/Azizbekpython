1.Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
a=8/0

Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    word=input("enter word:")
    number=int(input())
    print("number:",number)
except ValueError:
    print ("ValueError:","XATO")



Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
filename = input("Ochmoqchi bo'lgan fayl nomini kiriting: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("Fayl muvaffaqiyatli ochildi. Mazmuni:")
        print(content)
except FileNotFoundError:
    print(f"Xato: '{filename}' nomli fayl topilmadi.")
Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
try:
    num1=input("enter number:")
    num2=input("enter number")
    n1=float(num1)
    n2=float(num2)
    print(f"siz kiritgan son:{n1}va{n2}")
except ValueError:
    raise TypeError("Xato: Siz son bo'lmagan qiymat kiritdingiz!")

Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
def open_file_with_permission_check(filename):
    try:
        # Trying to open the file for writing
        with open(filename, 'w') as file:
            file.write("This is a test line.\n")
        print("File written successfully.")
    except PermissionError:
        print(f"Permission denied: Cannot write to the file '{filename}'.")

# Example usage
filename = input("Enter the filename to open: ")
open_file_with_permission_check(filename)
Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
def access_list_element(my_list, index):
    try:
        element = my_list[index]
        print(f"Element at index {index}: {element}")
    except IndexError:
        print(f"IndexError: The index {index} is out of range for the list.")

# Example usage
my_list = [10, 20, 30, 40, 50]
print(f"List: {my_list}")

try:
    index = int(input("Enter the index you want to access: "))
    access_list_element(my_list, index)
except ValueError:
    print("Invalid input: Please enter an integer index.")
def get_user_number():
    try:
        number = float(input("Please enter a number: "))
        print(f"You entered: {number}")
    except KeyboardInterrupt:
        print("\nInput cancelled by the user.")
    except ValueError:
        print("Invalid input: Please enter a valid number.")
def safe_division(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ArithmeticError as e:
        print(f"Arithmetic error occurred: {e}")

# Example usage
try:
    num1 = float(input("Enter numerator: "))
    num2 = float(input("Enter denominator: "))
    safe_division(num1, num2)
except ValueError:
    print("Invalid input: Please enter numbers.")
def read_file_safely(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print("File content:")
            print(content)
    except UnicodeDecodeError:
        print(f"UnicodeDecodeError: Could not decode the file '{filename}' with UTF-8 encoding.")
    except FileNotFoundError:
        print(f"FileNotFoundError: The file '{filename}' does not exist.")

# Example usage
filename = input("Enter the filename to open: ")
read_file_safely(filename)
def list_operation_with_attribute_error(my_list):
    try:
        # Let's attempt to call a non-existent method 'non_existent_method'
        my_list.non_existent_method()
    except AttributeError:
        print("AttributeError: The list object has no such attribute or method.")

# Example usage
my_list = [1, 2, 3]
list_operation_with_attribute_error(my_list)
Write a Python program to read an entire text file.
try:
    fayl = input("Enter file name: ")
    with open(fayl, 'r', encoding='utf-8') as f:
        matn = f.read()
        print("Fayl mazmuni:")
        print(matn)
except FileNotFoundError:
    print(f"Xato: '{fayl}' nomli fayl topilmadi.")
except UnicodeDecodeError:
    print(f"Xato: '{fayl}' faylini UTF-8 kodlash bilan o'qib bo'lmadi.")
except Exception as x:
    print(f"Boshqa xato: {x}")
def read_first_n_lines(filename, n):
    with open(filename, 'r') as f:
        for i in range(n):
            line = f.readline()
            if not line:
                break
            print(line.strip())
2️⃣ Append text to a file and display the text
python
Копировать
Редактировать
def append_and_display(filename, text):
    with open(filename, 'a') as f:
        f.write(text + '\n')
    with open(filename, 'r') as f:
        print(f.read())
3️⃣ Read last n lines of a file
python
Копировать
Редактировать
def read_last_n_lines(filename, n):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines[-n:]:
            print(line.strip())
4️⃣ Read line by line and store into a list
python
Копировать
Редактировать
def file_to_list(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]
    return lines
5️⃣ Read line by line and store into a variable
python
Копировать
Редактировать
def file_to_variable(filename):
    with open(filename, 'r') as f:
        content = f.read()
    return content
6️⃣ Read line by line and store into an array (list)
python
Копировать
Редактировать
# Same as 4️⃣
7️⃣ Find longest words
python
Копировать
Редактировать
def find_longest_words(filename):
    with open(filename, 'r') as f:
        words = f.read().split()
    max_len = max(len(word) for word in words)
    longest = [word for word in words if len(word) == max_len]
    return longest
8️⃣ Count number of lines in a file
python
Копировать
Редактировать
def count_lines(filename):
    with open(filename, 'r') as f:
        return sum(1 for _ in f)
9️⃣ Count frequency of words
python
Копировать
Редактировать
from collections import Counter

def word_frequency(filename):
    with open(filename, 'r') as f:
        words = f.read().split()
    return Counter(words)
🔟 Get file size
python
Копировать
Редактировать
import os

def file_size(filename):
    return os.path.getsize(filename)
1️⃣1️⃣ Write list to a file
python
Копировать
Редактировать
def write_list_to_file(filename, data):
    with open(filename, 'w') as f:
        for item in data:
            f.write(str(item) + '\n')
1️⃣2️⃣ Copy contents to another file
python
Копировать
Редактировать
def copy_file(src, dest):
    with open(src, 'r') as f1, open(dest, 'w') as f2:
        f2.write(f1.read())
1️⃣3️⃣ Combine lines from two files
python
Копировать
Редактировать
def combine_lines(file1, file2, out_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(out_file, 'w') as out:
        for l1, l2 in zip(f1, f2):
            out.write(l1.strip() + ' ' + l2)
1️⃣4️⃣ Read random line
python
Копировать
Редактировать
import random

def random_line(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return random.choice(lines).strip()
1️⃣5️⃣ Check if file is closed
python
Копировать
Редактировать
f = open('example.txt', 'r')
print(f.closed)  # False
f.close()
print(f.closed)  # True
1️⃣6️⃣ Remove newlines
python
Копировать
Редактировать
def remove_newlines(filename):
    with open(filename, 'r') as f:
        content = f.read().replace('\n', '')
    return content
1️⃣7️⃣ Count words in file (commas may separate words)
python
Копировать
Редактировать
def count_words(filename):
    with open(filename, 'r') as f:
        text = f.read().replace(',', ' ')
        words = text.split()
    return len(words)
1️⃣8️⃣ Extract characters to a list
python
Копировать
Редактировать
def extract_characters(filenames):
    chars = []
    for file in filenames:
        with open(file, 'r') as f:
            chars.extend(list(f.read()))
    return chars
1️⃣9️⃣ Generate A.txt to Z.txt
python
Копировать
Редактировать
import string

def generate_files():
    for letter in string.ascii_uppercase:
        with open(f'{letter}.txt', 'w') as f:
            f.write(f"This is {letter}.txt\n")
2️⃣0️⃣ Alphabet file with specified letters per line
python
Копировать
Редактировать
def alphabet_file(filename, letters_per_line):
    import string
    with open(filename, 'w') as f:
        alphabet = string.ascii_lowercase
        for i in range(0, len(alphabet), letters_per_line):
            f.write(alphabet[i:i+letters_per_line] + '\n')
