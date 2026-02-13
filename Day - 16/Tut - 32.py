# ==========================================
# PYTHON DICTIONARY BASICS
# ==========================================

# A dictionary is a built-in data type in Python.
# It stores data in KEY : VALUE pairs.
# Dictionaries are written using curly braces { }

# Example of a simple dictionary
student = {
    "name": "Alice",     # key = "name", value = "Alice"
    "age": 20,           # key = "age", value = 20
    "course": "Python"   # key = "course", value = "Python"
}

# ------------------------------------------
# IMPORTANT POINTS ABOUT DICTIONARIES
# ------------------------------------------

# 1. Keys must be unique.
# If you repeat a key, the last value will overwrite the previous one.

example = {
    "a": 10,
    "a": 20   # This overwrites the previous "a": 10
}

# 2. Keys must be immutable (unchangeable types).
# Allowed: strings, numbers, tuples
# Not allowed: lists or other dictionaries as keys.

# 3. Values can be any data type.
# String, int, float, list, tuple, boolean, even another dictionary.

person = {
    "name": "John",
    "age": 25,
    "marks": [85, 90, 78],   # list as value
    "is_passed": True        # boolean as value
}

# ------------------------------------------
# HOW TO ACCESS VALUES IN A DICTIONARY
# ------------------------------------------

# You access dictionary values using their keys
# with square brackets []

print(student["name"])   # Output: Alice
print(student["age"])    # Output: 20

# IMPORTANT:
# If you try to access a key that does not exist,
# Python will give an error.

# Example (This will cause an error):
# print(student["grade"])

# ------------------------------------------
# DIFFERENCE BETWEEN LIST AND DICTIONARY
# ------------------------------------------

# List example
my_list = ["apple", "banana", "cherry"]

# Access list using index number
print(my_list[0])  # Output: apple

# Dictionary example
my_dict = {
    "fruit1": "apple",
    "fruit2": "banana"
}

# Access dictionary using key
print(my_dict["fruit1"])  # Output: apple

# ==========================================
# END OF FILE
# ==========================================