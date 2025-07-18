def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
Misollar:
python
Копировать
Редактировать
print(is_leap(2020))  # True
print(is_leap(1900))  # False
print(is_leap(2000))  # True
print(is_leap("2020"))  # ValueError: Year must be an integer.
n = int(input("Enter a number: "))

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")


a = int(input("Enter a: "))
b = int(input("Enter b: "))

evens = [x for x in range(min(a, b), max(a, b)+1) if x % 2 == 0]

print("Even numbers:", evens)
