"""
===========================================
INSTANCE VARIABLES vs CLASS VARIABLES
===========================================

This file explains the difference between:
1. Instance Variables
2. Class Variables

-------------------------------------------
1. INSTANCE VARIABLES
-------------------------------------------
- Defined inside methods (usually __init__)
- Belong to a specific object (instance)
- Each object has its own copy
- Changing one object’s variable does NOT affect others

-------------------------------------------
2. CLASS VARIABLES
-------------------------------------------
- Defined inside the class but outside methods
- Shared among ALL instances of the class
- Only one copy exists
- Changing it affects all objects (unless overridden)

-------------------------------------------
EXAMPLE CLASS
-------------------------------------------
"""

class Student:
    # CLASS VARIABLE (shared by all students)
    school_name = "ABC School"

    def __init__(self, name, marks):
        # INSTANCE VARIABLES (unique for each student)
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}, School: {Student.school_name}")


# -------------------------------------------
# CREATING OBJECTS
# -------------------------------------------
s1 = Student("Rahul", 85)
s2 = Student("Priya", 90)

print("Initial Data:")
s1.display()
s2.display()


# -------------------------------------------
# MODIFYING INSTANCE VARIABLE
# -------------------------------------------
print("\nChanging Rahul's marks (instance variable):")
s1.marks = 95

s1.display()
s2.display()

# Notice:
# Only Rahul's marks changed, Priya's marks remain same


# -------------------------------------------
# MODIFYING CLASS VARIABLE
# -------------------------------------------
print("\nChanging school name (class variable):")
Student.school_name = "XYZ School"

s1.display()
s2.display()

# Notice:
# School name changed for BOTH students


# -------------------------------------------
# OVERRIDING CLASS VARIABLE USING INSTANCE
# -------------------------------------------
print("\nOverriding class variable for one object:")

s1.school_name = "My Personal School"

s1.display()
s2.display()

# Explanation:
# s1 now has its own instance variable named 'school_name'
# s2 still uses the class variable


# -------------------------------------------
# ACCESSING VARIABLES
# -------------------------------------------
print("\nAccessing variables:")

# Access class variable
print("Class variable:", Student.school_name)

# Access instance variables
print("Instance variable (s1 name):", s1.name)
print("Instance variable (s2 marks):", s2.marks)


# -------------------------------------------
# SUMMARY
# -------------------------------------------
"""
INSTANCE VARIABLES:
- Defined using self (e.g., self.name)
- Unique for each object
- Stored inside the object

CLASS VARIABLES:
- Defined inside class, outside methods
- Shared among all objects
- Stored in the class

KEY DIFFERENCE:
- Instance variables → object-specific
- Class variables → shared across all objects
"""


# -------------------------------------------
# BONUS EXAMPLE
# -------------------------------------------
class Car:
    wheels = 4  # class variable

    def __init__(self, brand):
        self.brand = brand  # instance variable


c1 = Car("Toyota")
c2 = Car("Honda")

print("\nBonus Example:")
print(c1.brand, "has", c1.wheels, "wheels")
print(c2.brand, "has", c2.wheels, "wheels")

# Changing class variable
Car.wheels = 6

print("\nAfter changing wheels:")
print(c1.brand, "has", c1.wheels, "wheels")
print(c2.brand, "has", c2.wheels, "wheels")