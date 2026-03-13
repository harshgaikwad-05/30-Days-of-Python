"""
=========================================================
PYTHON FILE I/O (INPUT / OUTPUT) COMPLETE EXAMPLE
=========================================================

This file demonstrates the following concepts:

1. File Opening
2. File Reading
3. Reading line by line
4. Reading all lines
5. Writing to a file
6. Appending to a file
7. File pointer functions (tell, seek)
8. Exception handling
9. Best practice using 'with' statement

Author: Example Python Program
=========================================================
"""

# ------------------------------------------------------
# 1. WRITING TO A FILE
# ------------------------------------------------------
# Mode: 'w'
# - Creates a new file if it doesn't exist
# - Overwrites the file if it already exists

print("----- Writing to File -----")

with open("sample.txt", "w") as file:
    file.write("Hello World\n")
    file.write("Welcome to Python File Handling\n")
    file.write("This file is created using Python\n")

print("Data written successfully!\n")


# ------------------------------------------------------
# 2. READING ENTIRE FILE
# ------------------------------------------------------
# Mode: 'r'
# - Opens the file for reading

print("----- Reading Entire File -----")

with open("sample.txt", "r") as file:
    content = file.read()  # reads complete file

print(content)


# ------------------------------------------------------
# 3. READING FILE LINE BY LINE
# ------------------------------------------------------

print("----- Reading Line by Line -----")

with open("sample.txt", "r") as file:

    # Loop through each line in the file
    for line in file:
        print(line.strip())  # strip() removes newline characters

print()


# ------------------------------------------------------
# 4. READLINES() METHOD
# ------------------------------------------------------
# readlines() returns all lines as a list

print("----- Using readlines() -----")

with open("sample.txt", "r") as file:
    lines = file.readlines()

print("Lines as List:")
print(lines)
print()


# ------------------------------------------------------
# 5. APPENDING TO A FILE
# ------------------------------------------------------
# Mode: 'a'
# - Adds new data at the end of the file
# - Does NOT delete existing content

print("----- Appending Data -----")

with open("sample.txt", "a") as file:
    file.write("This line was appended later.\n")

print("Data appended successfully!\n")


# ------------------------------------------------------
# 6. FILE POINTER FUNCTIONS
# ------------------------------------------------------

print("----- File Pointer Example -----")

with open("sample.txt", "r") as file:

    print("Current Position:", file.tell())  # shows cursor position

    file.seek(6)  # move cursor to 6th character

    print("Position After seek():", file.tell())

    print("Reading from position 6:")
    print(file.read())

print()


# ------------------------------------------------------
# 7. EXCEPTION HANDLING
# ------------------------------------------------------
# Prevents program crash if file does not exist

print("----- Exception Handling -----")

try:
    with open("non_existing_file.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: File does not exist!")

except Exception as error:
    print("Unexpected Error:", error)

print()


# ------------------------------------------------------
# 8. FILE MODES SUMMARY
# ------------------------------------------------------

"""
Common File Modes:

'r'  -> Read file
'w'  -> Write file (overwrites)
'a'  -> Append to file
'x'  -> Create new file (error if exists)
'r+' -> Read and write
'rb' -> Read binary
'wb' -> Write binary
"""

print("Program Completed Successfully!")