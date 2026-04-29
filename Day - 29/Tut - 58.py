"""
===========================================
ACCESS MODIFIERS IN PYTHON (FULL GUIDE)
===========================================

Python does not have strict access modifiers like Java or C++.
Instead, it uses naming conventions to indicate access levels.

There are 3 types of access modifiers in Python:

1. Public
2. Protected (single underscore _)
3. Private (double underscore __)

NOTE:
These are conventions, not strict restrictions.
Python follows "consenting adults" philosophy.
"""


# ===========================================
# 1. PUBLIC MEMBERS
# ===========================================
class PublicExample:
    def __init__(self):
        self.name = "Public Variable"

    def display(self):
        print("This is a public method")


print("\n--- PUBLIC EXAMPLE ---")
obj = PublicExample()

# Accessing public variable
print(obj.name)

# Accessing public method
obj.display()


# ===========================================
# 2. PROTECTED MEMBERS (_ single underscore)
# ===========================================
class ProtectedExample:
    def __init__(self):
        self._age = 25  # Protected variable

    def _show_age(self):  # Protected method
        print("Age:", self._age)


print("\n--- PROTECTED EXAMPLE ---")
obj = ProtectedExample()

# Accessing protected members (possible but discouraged)
print(obj._age)
obj._show_age()


# ===========================================
# 3. PRIVATE MEMBERS (__ double underscore)
# ===========================================
class PrivateExample:
    def __init__(self):
        self.__salary = 50000  # Private variable

    def __show_salary(self):  # Private method
        print("Salary:", self.__salary)

    def access_private(self):
        """Public method to access private members"""
        self.__show_salary()


print("\n--- PRIVATE EXAMPLE ---")
obj = PrivateExample()

# Direct access (will fail)
# print(obj.__salary)  # Uncommenting this will raise AttributeError

# Correct way using public method
obj.access_private()


# ===========================================
# NAME MANGLING IN PRIVATE MEMBERS
# ===========================================
print("\n--- NAME MANGLING ---")

# Python internally changes __variable to _ClassName__variable
print(obj._PrivateExample__salary)


# ===========================================
# INHERITANCE WITH ACCESS MODIFIERS
# ===========================================

class Parent:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"

    def show(self):
        print("Parent Class Method")


class Child(Parent):
    def access_parent(self):
        print("\nInside Child Class:")

        # Public - Accessible
        print(self.public)

        # Protected - Accessible (but should be used carefully)
        print(self._protected)

        # Private - NOT directly accessible
        # print(self.__private)  # This will fail

        # Access using name mangling
        print(self._Parent__private)


print("\n--- INHERITANCE EXAMPLE ---")
child = Child()
child.access_parent()


# ===========================================
# SUMMARY
# ===========================================
"""
PUBLIC:
    - Accessible everywhere
    - No underscore

PROTECTED:
    - Indicated by single underscore (_var)
    - Should not be accessed outside class/subclass (but possible)

PRIVATE:
    - Indicated by double underscore (__var)
    - Not directly accessible
    - Uses name mangling (_ClassName__var)

IMPORTANT:
Python does not enforce strict access control.
These are conventions to guide developers.
"""