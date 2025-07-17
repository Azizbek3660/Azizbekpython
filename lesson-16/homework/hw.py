1. Convert List to 1D Array
Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

Expected Output:

Original List: [12.23, 13.32, 100, 36.32] One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]
import numpy as np
list=[12.23,13.32,100,36.32]
array1=np.array(list)
print("list:",list)
print("Numpy array:",array1)
2. Create 3x3 Matrix (2?10)
Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

Expected Output:

[[ 2 3 4] [ 5 6 7] [ 8 9 10]]
ls=[[2,3,4],[5,6,7],[8,9,10]]
array2=np.array(ls)
print(array2)
3. Null Vector (10) & Update Sixth Value
Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

[ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

Update sixth value to 11 [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
zeronumpy=np.zeros((10))
print(zeronumpy)
zeronumpy[6]=11
print(zeronumpy)
4. Array from 12 to 38
Write a NumPy program to create an array with values ranging from 12 to 38.

Expected Output:

[12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
num=np.arange(12,38)
print(num)
5. Convert Array to Float Type
Write a NumPy program to convert an array to a floating type.

Sample output:

Original array [1, 2, 3, 4]
array3=np.array([1,2,3,4])
print(array3)
float_array=array3.astype(float)
print(float_array)
6. Celsius to Fahrenheit Conversion
Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.

Sample Array [0, 12, 45.21, 34, 99.91] [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]

Expected Output:

Values in Fahrenheit degrees: [ 0. 12. 45.21 34. 99.91 32. ]

Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]

Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]

Values in Fahrenheit degrees: [-0. 12. 45.21 34. 99.91 32. ]
celsium=np.array([-17.78, -11.11,7.34, 1.11, 37.73, 0.])
fahrenheit=(celsium*9/5)+32
print(fahrenheit)

fah=np.array([0, 12, 45,21 ,34, 99,91 ,32,])
cel=(fah-32)*5/9
print(cel)
7. Append Values to Array (Do self-tudy)
Write a NumPy program to append values to the end of an array.

Expected Output:

Original array: [10, 20, 30]

After append values to the end of the array: [10 20 30 40 50 60 70 80 90]
arr1=([10,20,30])
arr2=(40,50,60,70,80,90)
arrs_append=np.append(arr1,arr2)
print(arrs_append)
8. Array Statistical Functions (Do self-tudy)
Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.
arr = np.random.randint(0, 100, 10)
print("Random Array:", arr)

# Statistika hisoblash
mean_val = np.mean(arr)
median_val = np.median(arr)
std_dev = np.std(arr)

# Natijalarni chiqarish
print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_dev)
9 Find min and max
Create a 10x10 array with random values and find the minimum and maximum values.
arr = np.random.randint(0, 100, (10, 10))
print("Random 10x10 Array:\n", arr)

# Minimum va maximum qiymatlarni topish
min_val = np.min(arr)
max_val = np.max(arr)

print("Minimum value:", min_val)
print("Maximum value:", max_val)
10
Create a 3x3x3 array with random values.
arr = np.random.randint(0, 100, (3, 3, 3))
print("3x3x3 Random Array:\n", arr)
