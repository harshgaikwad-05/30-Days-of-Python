"""
PYTHON BASICS - SINGLE FILE GUIDE
--------------------------------
This file explains important Python topics with simple examples.
Students can run this file and learn step by step.

Run using: python filename.py
"""

# -----------------------------
# 1. PRINT & BASIC OUTPUT
# -----------------------------
print("Hello, World!")  # This prints text on the screen


# -----------------------------
# 2. VARIABLES
# -----------------------------
name = "Alice"   # String (text)
age = 20         # Integer (whole number)
height = 5.6     # Float (decimal number)
is_student = True  # Boolean (True/False)

print("\nVariables:")
print(name, age, height, is_student)


# -----------------------------
# 3. DATA TYPES
# -----------------------------
print("\nData Types:")
print(type(name))       # str
print(type(age))        # int
print(type(height))     # float
print(type(is_student)) # bool


# -----------------------------
# 4. INPUT FROM USER
# -----------------------------
# Uncomment to try
# user_name = input("\nEnter your name: ")
# print("Hello,", user_name)


# -----------------------------
# 5. OPERATORS
# -----------------------------
a = 10
b = 3

print("\nOperators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)


# -----------------------------
# 6. CONDITIONAL STATEMENTS
# -----------------------------
print("\nConditionals:")
num = 5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# -----------------------------
# 7. LOOPS
# -----------------------------
print("\nFor Loop:")
for i in range(5):
    print(i)

print("\nWhile Loop:")
count = 0
while count < 3:
    print(count)
    count += 1


# -----------------------------
# 8. FUNCTIONS
# -----------------------------
def greet(name):
    return "Hello " + name

print("\nFunctions:")
print(greet("Alice"))


# -----------------------------
# 9. LISTS
# -----------------------------
numbers = [1, 2, 3, 4]

print("\nLists:")
print(numbers)
numbers.append(5)
print("After append:", numbers)
print("First element:", numbers[0])


# -----------------------------
# 10. TUPLES
# -----------------------------
tuple_data = (1, 2, 3)
print("\nTuples:")
print(tuple_data)


# -----------------------------
# 11. DICTIONARIES
# -----------------------------
student = {
    "name": "Alice",
    "age": 20
}

print("\nDictionaries:")
print(student)
print("Name:", student["name"])


# -----------------------------
# 12. SETS
# -----------------------------
unique_numbers = {1, 2, 3, 3}
print("\nSets:")
print(unique_numbers)  # duplicates removed


# -----------------------------
# 13. STRINGS
# -----------------------------
text = "Python"

print("\nStrings:")
print(text.lower())
print(text.upper())
print(text[0])  # first character


# -----------------------------
# 14. FILE HANDLING
# -----------------------------
print("\nFile Handling:")

# Write to file
with open("sample.txt", "w") as f:
    f.write("Hello file!")

# Read file
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)


# -----------------------------
# 15. EXCEPTION HANDLING
# -----------------------------
print("\nException Handling:")

try:
    x = int("abc")  # error
except ValueError:
    print("Conversion failed!")


# -----------------------------
# 16. CLASSES & OBJECTS
# -----------------------------
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is", self.name)

print("\nClasses & Objects:")
p1 = Person("Alice")
p1.say_hello()


# -----------------------------
# 17. MODULES (IMPORT)
# -----------------------------
import math

print("\nModules:")
print("Square root of 16:", math.sqrt(16))


# -----------------------------
# END
# -----------------------------
print("\n--- End of Python Basics ---")