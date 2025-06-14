1. Create and Access List Elements
Create a list containing five different fruits and pr

fruits=["apple","banan","orange","graperuit","mango"]
print (fruits[0]) 
print(fruits[3])
2. Concatenate Two Lists
Create two lists of numbers and concatenate them into a single list
list_1=[1,2,3,4,5,6]
list_2=[7,8,9,10]
combined_list=list_1+list_2
print (combined_list)
3. Extract Elements from a List
Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
list_3=[10,20,30,40,50]
first=list_3[0]
middle=list_3[len(list_3)//2]
last=list_3[-1]
result=[first,middle,last]

print(result)

4. Convert List to Tuple
Create a list of your five favorite movies and convert it into a tuple.
movies=['king of rings','jungle','poiro','agent 007','mission 01']
tuple_movies=tuple(movies)
print(tuple_movies)
5. Check Element in a List
Given a list of cities, check if "Paris" is in the list and print the result.
cities=["Russia","Paris","London","USA","Uzbekistan"]
if "Paris"  in cities:
    print ("Paris is in the list")
else:
    print("Paris is not in the list")
6. Duplicate a List Without Using Loops
Create a list of numbers and duplicate it without using loop
numbers=[1,2,3,4,5]
dublicated=(numbers*2)
print(dublicated)
7. Swap First and Last Elements of a List
Given a list of numbers, swap the first and last elements.
number=[1,2,3,4,5,6,7]
number[0],number[-1]=number[-1],number[0]
print(number)
8. Slice a Tuple
Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
nymbers=(1,2,3,4,5,6,7,8,9,10)
sliced=nymbers[3:7]
print(sliced)

9. Count Occurrences in a List
Create a list of colors and count how many times "blue" appear
colours=("red","blue","black","red","blue","blue")
count_blue=colours.count("blue")
print("Blue appears", count_blue, "times.")

10. Find the Index of an Element in a Tuple
Given a tuple of animals, find the index of "lion
animals=('cat','lion','dog','wolf')
lion_index=animals.index('lion')
print("The index of 'lion' is:", lion_index)
11. Merge Two Tuples
Create two tuples of numbers and merge them into a single tupl
list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list =list1+list2
print(merged_list)

12. Find the Length of a List and Tuple
Given a list and a tuple, find and print their lengths.
a=[1,2,3,4,5,6,7,8]
b=(9,10,11,12,13,14)
len_a=len(a)
len_b=len(b)
print("list_length:",len_a,"and","tuple_length:",len_b)
13. Convert Tuple to List
Create a tuple of five numbers and convert it into a list.
numbers=(1,2,3,4,5)
list_number=list(numbers)
print(list_number)
14. Find Maximum and Minimum in a Tuple
Given a tuple of numbers, find and print the maximum and minimum values.
tuple_numbers = (1,2,3,4,5,6)
max_value = max(tuple_numbers)
min_value = min(tuple_numbers)

print("Max number:", max_value)
print("Min number:", min_value)
15. Reverse a Tuple
Create a tuple of words and print it in reverse order.
words = ("apple", "banana", "cherry", "date")


reversed_words = words[::-1]


print(reversed_words)
