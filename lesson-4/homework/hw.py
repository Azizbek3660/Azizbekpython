1. Sort a Dictionary by Value
Write a Python script to sort (ascending and descending) a dictionary by value.
fruits={"banan":12,"apple":11,"apricot":5,"orange":8,"cherry":1}
sorted_asc = dict(sorted(fruits.items(), key=lambda item: item[1]))
print("Ascending:", sorted_asc)
sorted_desc = dict(sorted(fruits.items(), key=lambda item: item[1], reverse=True))
print("Descending:", sorted_desc)
2. Add a Key to a Dictionary
Write a Python script to add a key to a dictionary.

Sample Dictionary:

{0: 10, 1: 20}
Expected Result:

{0: 10, 1: 20, 2: 30}
number={0:10,1:20}
number[2]=20
print(number)
3. Concatenate Multiple Dictionaries
Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionaries:

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
Expected Result:

{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
merged_dict = {}
for d in (dic1, dic2, dic3):
    merged_dict.update(d)

print(merged_dict)

4. Generate a Dictionary with Squares
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

Sample Dictionary (n = 5):

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
n = 6
squares_dict = {}

for x in range(1, n+1):
    squares_dict[x] = x * x

print(squares_dict)

5. Dictionary of Squares (1 to 15)
Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

Expected Output:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
number= 15
squares_dict = {}

for x in range(1, number+1):
    squares_dict[x] = x * x

print(squares_dict)
1. Create a Set
Write a Python program to create a set.
set_cteate={'hello','man',1,23,4,5,6,(1,2,3,4,6,)}
print("set_create:",set_cteate)
2. Iterate Over a Set
Write a Python program to iterate over sets.
my_set = {"apple", "banana", "cherry"}


for fruit in my_set:
    print(fruit)
3. Add Member(s) to a Set
Write a Python program to add member(s) to a set.
number={1,2,3,4,5,6,}
number.add(10)
print(number)
4. Remove Item(s) from a Set
Write a Python program to remove item(s) from a given set.
number={1,2,3,4,5,6,7,8}
number.remove(8)
print(number)
5. Remove an Item if Present in the Set
Write a Python program to remove an item from a set if it is present in the set.
my_set = {"apple", "banana", "cherry"}

my_set.discard("banana")

print(my_set)
