1. Circle Class
Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math
class Circle:
    def __init__(self ,radius):
        self.radius=radius
    def get_area(self):
        return math.pi*(self.radius**2)
    def get_perimetr(self):
        return 2*math.pi*self.radius
radius = float(input("Doira radiusini kiriting: "))
circle=Circle(radius)
print(f'doira yuzasi:{circle.get_area():.2f}')
print(f'doira perimetri:{circle.get_perimetr():.2f}')



2. Person Class
Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.
import datetime
class Person:
    def __init__(self,name,country,date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth=date_of_birth
    def get_age(self):  
        today = datetime.date.today()
        birth = self.date_of_birth
        age = today.year - birth.year  
        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1

        return age 
name=input("enter name:")
country=input("enter country:")
yil=int(input("enter yil"))
oy=int(input("enter oy (1-15): "))
kun=int(input("enter kun:"))
dob = datetime.date(yil, oy, kun)
person=Person(name,country,dob)
print(f"\n{person.name} ({person.country}) hozirda {person.get_age()} yoshda.")


3. Calculator Class
Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.
class Calculator:
    def add_numbers(a,b):
        return a+b
    def subtract_numbers(a,b):
        return a-b
    def multiply_numbers(a,b):
        return a*b
    def divide_numbers (a,b):
        return a/b
c=Calculator.add_numbers(10,15)
print (c)

4. Shape and Subclasses
Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.
import math
class Shape:
    def area(self):
        raise NotImplementedError
    def perimetr(self):
        raise NotImplementedError
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
    def perimetr(self):
        return 2*math.pi*self.radius
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2
    def perimetr(self):
        return 4*self.side
class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def perimetr(self):
        return self.a+self.b+self.c
    def area (self):
        s = self.perimetr() / 2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
circle=Circle(4)
Square=Square(4)
Triangle=Triangle(3,4,4)
print("Circle: area=",circle.area(),"Perimetr=",circle.perimetr())

print("Square: area=",Square.area(),"Perimetr=",Square.perimetr())

print("Triangle: area=",Triangle.area(),"Perimetr=",Triangle.perimetr())


        

5. Binary Search Tree Class
Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Boshlanish nuqtasi
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            # Chapga joylash
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            # O‘ngga joylash
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert_recursive(node.right, value)
        else:
            # Dublikat qiymat — qo‘shilmaydi
            print(f"{value} allaqachon mavjud")

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
🔍 Foydalanish misoli:
python
Копировать код
# Daraxt yaratish
bst = BinarySearchTree()

# Qiymatlarni qo‘shish
for val in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(val)

# Qidirish
print("60 bormi?", bst.search(60))  # True
print("25 bormi?", bst.search(25))  # False

# Inorder chiqarish (saralangan tartibda)
print("Inorder:", bst.inorder())  # [20, 30, 40, 50, 60, 70, 80]
6. Stack Data Structure
Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  # Yangi element qo‘shish

    def pop(self):
        if self.is_empty():
            return "Stack bo‘sh, pop qilish mumkin emas!"
        return self.items.pop()  # Oxirgi elementni olib tashlash

    def peek(self):
        if self.is_empty():
            return "Stack bo‘sh!"
        return self.items[-1]  # Eng yuqoridagi elementni ko‘rsatadi

    def is_empty(self):
        return len(self.items) == 0  # Bo‘shlikni tekshiradi

    def size(self):
        return len(self.items)  # Elementlar soni
🔍 Misol:
python
Копировать код
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Eng yuqoridagi:", stack.peek())  # 30
print("Pop qilindi:", stack.pop())      # 30
print("Pop qilindi:", stack.pop())      # 20
print("Stack bo‘shmi?", stack.is_empty())  # False
print("Pop qilindi:", stack.pop())      # 10
print("Pop qilindi:", stack.pop())      # Stack bo‘sh!
7. Linked List Data Structure
Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.
# 1. Tugun klassi
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 2. Linked List klassi
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # Birinchi element bo‘lsa
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node  # Oxiriga qo‘shadi

    def delete(self, data):
        current = self.head
        prev = None

        while current:
            if current.data == data:
                if prev is None:
                    self.head = current.next  # Birinchi tugun o‘chirilsa
                else:
                    prev.next = current.next  # O‘rtadagi tugun o‘chirilsa
                return True  # O‘chirish muvaffaqiyatli
            prev = current
            current = current.next
        return False  # Topilmadi

    def display(self):
        current = self.head
        if not current:
            print("Linked list bo‘sh")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
🔍 Misol:
python
Копировать код
# Linked list yaratish
ll = LinkedList()

# Elementlar qo‘shish
ll.insert(10)
ll.insert(20)
ll.insert(30)

# Ko‘rsatish
ll.display()  # 10 -> 20 -> 30 -> None

# O‘chirish
ll.delete(20)

# Yana ko‘rsatish
ll.display()  # 10 -> 30 -> None
class ShoppingCart:
    def __init__(self):
        self.items = []  # Savatchadagi mahsulotlar ro'yxati

    def add_item(self, name, price, quantity=1):
        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })

    def remove_item(self, name):
        for item in self.items:
            if item['name'] == name:
                self.items.remove(item)
                return True  # Muvaffaqiyatli o‘chirildi
        return False  # Mahsulot topilmadi

    def total_price(self):
        total = 0
        for item in self.items:
            total += item['price'] * item['quantity']
        return total

    def show_cart(self):
        if not self.items:
            print("Savatcha bo‘sh.")
            return
        print("Savatchadagi mahsulotlar:")
        for item in self.items:
            print(f"- {item['name']} (narx: {item['price']}, miqdor: {item['quantity']})")
        print(f"Umumiy narx: {self.total_price()}")
class Customer:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} so‘m hisobga qo‘shildi.")
        else:
            print("Notog‘ri summa!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} so‘m yechildi.")
        else:
            print("Yetarli mablag‘ yo‘q yoki noto‘g‘ri summa!")

    def get_balance(self):
        return self.balance


class Bank:
    def __init__(self):
        self.customers = {}  # account_number -> Customer

    def create_account(self, name, account_number):
        if account_number in self.customers:
            print("Bu hisob raqami allaqachon mavjud.")
        else:
            self.customers[account_number] = Customer(name, account_number)
            print(f"{name} uchun hisob yaratildi.")

    def deposit_to_account(self, account_number, amount):
        customer = self.customers.get(account_number)
        if customer:
            customer.deposit(amount)
        else:
            print("Hisob raqami topilmadi.")

    def withdraw_from_account(self, account_number, amount):
        customer = self.customers.get(account_number)
        if customer:
            customer.withdraw(amount)
        else:
            print("Hisob raqami topilmadi.")

    def check_balance(self, account_number):
        customer = self.customers.get(account_number)
        if customer:
            print(f"{customer.name} balans: {customer.get_balance()} so‘m")
        else:
            print("Hisob raqami topilmadi.")
