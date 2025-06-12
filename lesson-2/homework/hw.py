##homework_2
1. Age Calculator
Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
from datetime import date
name=input("Ismingizni kiriting:")
birth_year=int(input("tugilgan yilingizni kiriting:"))
current_year=date.today().year
age=current_year-birth_year
print(f"salom,{name}! Sizning yoshingiz:{age} yosh.")
2. Extract Car Names
Extract car names from the following text:

txt = 'LMaasleitbtui'

txt = 'LMaasleitbtui'
txt[::2]
txt = 'LMaasleitbtui'
txt[1::2]
3. Extract Car Names
Extract car names from the following text:

txt = 'MsaatmiazD'
txt = 'MsaatmiazD'
txt[::2]
txt = 'MsaatmiazD'
txt[::-2]
4. Extract Residence Area
Extract the residence area from the following text:

txt = "I'am John. I am from London"
txt = "I'am John. I am from London"
print("I'am John.\n I am from London")
5. Reverse String
Write a Python program that takes a user input string and prints it in reverse order.
right_string=input('enter right_string')
reverse_string=right_string[::-1]
print("reverse_string:",reverse_string)
6. Count Vowels
Write a Python program that counts the number of vowels in a given string.
text=input("Enter a string: ")
vowels="euioaEUIOA"
count=sum(1 for char in text if  char in vowels )
print("count_vowels:",count)
7. Find Maximum Value
Write a Python program that takes a list of numbers as input and prints the maximum value.
list_number=input("enter list_number")
max_number=max(list_number)
print("max_number:",max_number)

8. Check Palindrome
Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
text=input("enter text")
if text == text[::-1]:
     print("bu soz palindrom:")
else:
     print("bu soz palindrom emas")
9. Extract Email Domain
Write a Python program that extracts and prints the domain from an email address provided by the user.
email = input("Enter your email address: ")

try:
    domain = email.split('@')[1]
    print("Domain:", domain)
except IndexError:
    print("Invalid email address. Please include '@'.")
10. Generate Random Password
Write a Python program to generate a random password containing letters, digits, and special characters.
import random
import string

password_length = 12

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(password_length))

print("Randomly generated password:", password)
