"""
Topic: dir(), __dict__, and help() in Python

This file demonstrates three important introspection tools in Python:
1. dir()     -> Lists attributes and methods of an object
2. __dict__  -> Shows an object's writable attributes (namespace)
3. help()    -> Displays documentation for objects

Run this file to see examples and outputs.
"""

# ----------------------------------------
# 1. dir() FUNCTION
# ----------------------------------------

def demonstrate_dir():
    print("\n--- dir() DEMONSTRATION ---")

    x = 10
    print("\ndir(x) where x = 10:")
    print(dir(x))  # Shows all attributes and methods of integer

    text = "hello"
    print("\ndir(text) where text = 'hello':")
    print(dir(text))  # String methods

    print("\ndir() without arguments (current scope):")
    print(dir())  # Names in current scope


# ----------------------------------------
# 2. __dict__ ATTRIBUTE
# ----------------------------------------

class Student:
    school_name = "ABC School"  # class attribute

    def __init__(self, name, marks):
        self.name = name        # instance attribute
        self.marks = marks      # instance attribute


def demonstrate_dict():
    print("\n--- __dict__ DEMONSTRATION ---")

    s1 = Student("Alice", 90)

    print("\ns1.__dict__ (instance namespace):")
    print(s1.__dict__)  # instance attributes only

    print("\nStudent.__dict__ (class namespace):")
    print(Student.__dict__)  # includes methods, class attributes

    # Adding attribute dynamically
    s1.grade = "A"
    print("\nAfter adding s1.grade = 'A':")
    print(s1.__dict__)


# ----------------------------------------
# 3. help() FUNCTION
# ----------------------------------------

def demonstrate_help():
    print("\n--- help() DEMONSTRATION ---")

    print("\nHelp on built-in function len:")
    help(len)

    print("\nHelp on string class:")
    help(str)

    print("\nHelp on custom class Student:")
    help(Student)


# ----------------------------------------
# MAIN EXECUTION
# ----------------------------------------

def main():
    print("PYTHON INTROSPECTION TOOLS DEMO")
    print("=" * 40)

    demonstrate_dir()
    demonstrate_dict()
    demonstrate_help()

    print("\n--- SUMMARY ---")
    print("""
dir()      -> Lists attributes and methods of an object
__dict__   -> Shows object's namespace (attributes stored)
help()     -> Provides documentation of objects
""")


if __name__ == "__main__":
    main()