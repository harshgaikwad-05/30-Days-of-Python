"""
File: file_read_methods.py
Topic: read() and readlines() in Python

This file demonstrates two commonly used file reading methods in Python:
1. read()
2. readlines()

Both methods are used after opening a file using the open() function.

Syntax to open a file:
    file_object = open("filename.txt", "mode")

Common modes:
    "r"  -> read mode (default)
    "w"  -> write mode
    "a"  -> append mode
"""

# ------------------------------------------------------------
# 1. read() METHOD
# ------------------------------------------------------------

"""
The read() method reads the entire content of a file as a single string.

Syntax:
    file_object.read(size)

Parameters:
    size (optional) -> number of characters to read.
                       If not specified, it reads the entire file.

Return Type:
    String

Use Case:
    When you want the entire file content as one string.
"""

# Example 1: Reading entire file
file = open("sample.txt", "r")  # open file in read mode

content = file.read()           # read the whole file

print("Using read():")
print(content)

file.close()                    # always close the file


# ------------------------------------------------------------
# Example 2: Reading limited characters
# ------------------------------------------------------------

file = open("sample.txt", "r")

partial_content = file.read(10)  # read first 10 characters

print("\nReading first 10 characters using read():")
print(partial_content)

file.close()


# ------------------------------------------------------------
# 2. readlines() METHOD
# ------------------------------------------------------------

"""
The readlines() method reads the file and returns a list of lines.

Syntax:
    file_object.readlines()

Return Type:
    List of strings (each element is a line from the file)

Important:
    Each line usually contains a newline character '\n' at the end.
"""

# Example 3: Reading all lines into a list

file = open("sample.txt", "r")

lines = file.readlines()  # returns list of lines

print("\nUsing readlines():")
print(lines)

file.close()


# ------------------------------------------------------------
# Example 4: Iterating through lines
# ------------------------------------------------------------

file = open("sample.txt", "r")

lines = file.readlines()

print("\nPrinting lines one by one:")

for line in lines:
    print(line.strip())  # strip() removes newline characters

file.close()


# ------------------------------------------------------------
# BETTER PRACTICE (Using 'with' statement)
# ------------------------------------------------------------

"""
Using 'with' automatically closes the file after execution.
This is the recommended approach in Python.
"""

# Example 5: Using read() with 'with'

with open("sample.txt", "r") as file:
    data = file.read()
    print("\nUsing with + read():")
    print(data)


# Example 6: Using readlines() with 'with'

with open("sample.txt", "r") as file:
    lines = file.readlines()

    print("\nUsing with + readlines():")
    for line in lines:
        print(line.strip())


# ------------------------------------------------------------
# Difference Between read() and readlines()
# ------------------------------------------------------------

"""
read()
------
• Returns the entire file as one single string.
• Can optionally read specific number of characters.
• Good for small files or when string processing is needed.

Example output:
    "Hello\nWelcome to Python\nFile Handling"

readlines()
-----------
• Returns a list where each element is a line.
• Easier to process line-by-line.
• Good for structured files like logs or CSV.

Example output:
    ["Hello\n", "Welcome to Python\n", "File Handling\n"]
"""

# End of File