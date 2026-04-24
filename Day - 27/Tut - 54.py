"""
Topic: Constructors in Python
---------------------------------
A constructor is a special method used to initialize objects.
In Python, the constructor method is called __init__().

Key Points:
1. Automatically called when an object is created.
2. Used to initialize attributes (variables) of a class.
3. Can take arguments (parameters).
"""

# ---------------------------------
# 1. Basic Constructor Example
# ---------------------------------

class Student:
    def __init__(self):
        print("Constructor called! Object created.")

# Creating an object
s1 = Student()

print("\n" + "-"*50 + "\n")

# ---------------------------------
# 2. Constructor with Parameters
# ---------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name   # instance variable
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects with values
s2 = Student("Amit", 20)
s3 = Student("Neha", 22)

s2.display()
s3.display()

print("\n" + "-"*50 + "\n")

# ---------------------------------
# 3. Default Constructor vs Parameterized Constructor
# ---------------------------------

class Example:
    def __init__(self, value=0):
        self.value = value

    def show(self):
        print("Value:", self.value)

# Using default value
e1 = Example()
e1.show()

# Using custom value
e2 = Example(100)
e2.show()

print("\n" + "-"*50 + "\n")

# ---------------------------------
# 4. Constructor with Different Data Types
# ---------------------------------

class Car:
    def __init__(self, brand, price, is_electric):
        self.brand = brand
        self.price = price
        self.is_electric = is_electric

    def details(self):
        print(f"Brand: {self.brand}")
        print(f"Price: {self.price}")
        print(f"Electric: {self.is_electric}")

c1 = Car("Tesla", 5000000, True)
c1.details()

print("\n" + "-"*50 + "\n")

# ---------------------------------
# 5. Constructor in Inheritance
# ---------------------------------

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # calling parent constructor
        self.subject = subject

    def show(self):
        print(f"Name: {self.name}, Subject: {self.subject}")

t1 = Teacher("Mr. Sharma", "Math")
t1.show()

print("\n" + "-"*50 + "\n")

# ---------------------------------
# 6. Multiple Constructors? (Using Default Arguments)
# ---------------------------------

class Demo:
    def __init__(self, a=None, b=None):
        if a is not None and b is not None:
            print("Two parameters:", a, b)
        elif a is not None:
            print("One parameter:", a)
        else:
            print("No parameters")

d1 = Demo()
d2 = Demo(10)
d3 = Demo(10, 20)

print("\n" + "-"*50 + "\n")

# ---------------------------------
# 7. Destructor (Bonus Concept)
# ---------------------------------

class Test:
    def __init__(self):
        print("Constructor: Object Created")

    def __del__(self):
        print("Destructor: Object Destroyed")

t = Test()
del t  # explicitly deleting object

print("\n" + "-"*50 + "\n")

# ---------------------------------
# Summary
# ---------------------------------
"""
Summary:
- __init__() is the constructor in Python.
- It initializes object properties.
- Can accept arguments.
- Used in inheritance with super().
- Python does not support multiple constructors directly,
  but we can simulate them using default arguments.

Practice:
Try creating your own class with a constructor that:
1. Stores student marks
2. Calculates average
3. Prints grade
"""