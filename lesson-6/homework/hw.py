def insert_underscore(txt):
    result = ""
    count = 0
    i = 0

    while i < len(txt):
        result += txt[i]
        count += 1

        if count == 3:
            # Tekshiramiz: keyingi belgidan keyin underscore kerakmi?
            next_i = i + 1
            if next_i < len(txt):
                if txt[next_i] in 'aeiou' or txt[next_i] == '_':
                    # Agar keyingi belgi unli yoki _ bo'lsa, shift qilamiz
                    result += txt[next_i]
                    i += 1
            result += "_"
            count = 0

        i += 1
    
    # Oxirida agar _ oxirga tushib qolsa, olib tashlaymiz
    if result.endswith("_"):
        result = result[:-1]

    return result
n=int(input())
for i in range(n):
    print(i**2)

a=1
while a<11:
    print (a)
    a=a+1
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print (j,end=' ')
    print()









num=int(input("enter number:"))
sum=0
for i in range(1,num+1):
    sum+=i
print("sum is:",sum)

n=int(input())
for i in range(1,11):
    print(n*i)
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num>50 and num<180:
        print(num)
num = input("Enter number: ")
print("Total digits:", len(num))
n=5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)

n = -10
while n<0:
    print(n)
    n=n+1
for i in range(5):
    print(i)
else:
    print ("done!")
start = 25
end = 50

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
n_terms = 10
n1, n2 = 0, 1
count = 0

print("Fibonacci sequence:")

while count < n_terms:
    print(n1, end=" ")
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
n=int(input())
factorial=1
for i in range(1,n+1):
    factorial*=i
print(f"{n}!={factorial}")
def uncommon_elements(list1, list2):
    result = []
    
    # list1 dagi elementlar list2 da yo'q bo'lsa
    temp_list2 = list2.copy()
    for item in list1:
        if item in temp_list2:
            temp_list2.remove(item)
        else:
            result.append(item)
    
    # list2 dagi qolgan elementlar
    result.extend(temp_list2)
    
    return result

# Misollar:
print(uncommon_elements([1, 1, 2], [2, 3, 4]))         # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))         # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5])) # [1, 2, 2, 5]
