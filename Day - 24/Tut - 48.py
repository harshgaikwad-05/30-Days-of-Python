"""
Python File Reading Examples
Topic: read() and readlines()

This file explains how to read data from a text file using:
1. read()
2. readlines()

Create a sample file named "sample.txt" in the same folder
and write some lines in it like:

Hello Students
Welcome to Python class
We are learning File Handling
This is the fourth line
"""

# -------------------------------------------------
# Example 1 : Using read()
# -------------------------------------------------

print("----- Example 1 : read() -----")

file = open("sample.txt", "r")   # open file in read mode

content = file.read()            # reads the entire file

print("Content of file using read():")
print(content)

file.close()                     # close the file


# -------------------------------------------------
# Example 2 : Using read(size)
# -------------------------------------------------

print("\n----- Example 2 : read(size) -----")

file = open("sample.txt", "r")

content = file.read(10)          # reads first 10 characters

print("First 10 characters of file:")
print(content)

file.close()


# -------------------------------------------------
# Example 3 : Using readlines()
# -------------------------------------------------

print("\n----- Example 3 : readlines() -----")

file = open("sample.txt", "r")

lines = file.readlines()         # reads all lines and stores them in a list

print("Lines returned by readlines():")
print(lines)

file.close()


# -------------------------------------------------
# Example 4 : Accessing lines from readlines()
# -------------------------------------------------

print("\n----- Example 4 : Access individual lines -----")

file = open("sample.txt", "r")

lines = file.readlines()

print("First line :", lines[0])
print("Second line:", lines[1])

file.close()


# -------------------------------------------------
# Example 5 : Using loop with readlines()
# -------------------------------------------------

print("\n----- Example 5 : Loop through lines -----")

file = open("sample.txt", "r")

lines = file.readlines()

for line in lines:
    print(line.strip())  # strip() removes newline characters

file.close()


# -------------------------------------------------
# Summary
# -------------------------------------------------

print("\n----- Summary -----")
print("read()      -> Reads entire file as a single string")
print("read(size)  -> Reads specific number of characters")
print("readlines() -> Reads all lines and returns a list")