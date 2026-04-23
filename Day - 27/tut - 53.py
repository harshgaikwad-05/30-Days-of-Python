"""
CLASSES AND OBJECTS IN PYTHON
----------------------------

A class is like a blueprint for creating objects.
An object is an instance of a class.

Think of it like this:
- Class = Design of a car
- Object = Actual car built using that design
"""

# -----------------------------
# 1. BASIC CLASS AND OBJECT
# -----------------------------

class Car:
    # Constructor method (called automatically when object is created)
    def __init__(self, brand, model):
        self.brand = brand      # instance variable
        self.model = model

    # Method (function inside class)
    def display_info(self):
        print(f"Car: {self.brand} {self.model}")


# Creating objects (instances)
car1 = Car("Toyota", "Corolla")
car2 = Car("Tesla", "Model 3")

car1.display_info()
car2.display_info()


# -----------------------------
# 2. INSTANCE VARIABLES vs CLASS VARIABLES
# -----------------------------

class Student:
    school_name = "ABC School"  # class variable (shared by all objects)

    def __init__(self, name, marks):
        self.name = name        # instance variable (unique per object)
        self.marks = marks

    def show(self):
        print(f"{self.name} scored {self.marks} marks at {Student.school_name}")


s1 = Student("Amit", 85)
s2 = Student("Riya", 92)

s1.show()
s2.show()


# -----------------------------
# 3. METHODS: INSTANCE, CLASS, STATIC
# -----------------------------

class Example:
    count = 0

    def __init__(self):
        Example.count += 1

    # Instance method (uses self)
    def instance_method(self):
        print("This is an instance method")

    # Class method (uses cls)
    @classmethod
    def class_method(cls):
        print(f"Total objects created: {cls.count}")

    # Static method (no self or cls)
    @staticmethod
    def static_method():
        print("This is a static method")


e1 = Example()
e2 = Example()

e1.instance_method()
Example.class_method()
Example.static_method()


# -----------------------------
# 4. ENCAPSULATION (PRIVATE VARIABLES)
# -----------------------------

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc = BankAccount(1000)
acc.deposit(500)
print("Balance:", acc.get_balance())

# print(acc.__balance)  # This will cause error (private)


# -----------------------------
# 5. INHERITANCE
# -----------------------------

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print("Dog barks")


a = Animal()
d = Dog()

a.speak()
d.speak()


# -----------------------------
# 6. POLYMORPHISM
# -----------------------------

class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

b = Bird()
p = Penguin()

b.fly()
p.fly()


# -----------------------------
# 7. SPECIAL METHOD (__str__)
# -----------------------------

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person name is {self.name}"


p1 = Person("Rahul")
print(p1)  # Calls __str__ automatically


# -----------------------------
# SUMMARY
# -----------------------------
"""
Key Points:
- Class = Blueprint
- Object = Instance of class
- __init__ = Constructor
- self = Refers to current object
- Methods = Functions inside class
- Inheritance = Reuse code
- Encapsulation = Hide data
- Polymorphism = Same method, different behavior
"""