"""
File: seek_and_tell_demo.py

Description:
This script demonstrates the use of seek() and tell() functions in Python file handling.

- tell()  -> Returns the current position of the file pointer.
- seek()  -> Moves the file pointer to a specified location.

Author: Your Name
Date: 2026
"""

# ------------------------------------------------------------
# STEP 1: Create and write to a sample file
# ------------------------------------------------------------

with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("We are learning seek() and tell().\n")
    file.write("Python file handling is powerful.\n")

print("Sample file created and data written.\n")


# ------------------------------------------------------------
# STEP 2: Open file in read mode
# ------------------------------------------------------------

with open("sample.txt", "r") as file:

    # --------------------------------------------------------
    # Using tell()
    # --------------------------------------------------------
    print("Initial file pointer position:", file.tell())
    # Output: 0 (beginning of file)

    # Read first 5 characters
    data = file.read(5)
    print("\nRead first 5 characters:", data)

    # Check position after reading
    print("File pointer after reading 5 characters:", file.tell())

    # --------------------------------------------------------
    # Using seek()
    # --------------------------------------------------------

    # Move pointer back to beginning
    file.seek(0)
    print("\nPointer moved back to start using seek(0)")
    print("Current position:", file.tell())

    # Read entire first line
    line = file.readline()
    print("\nFirst line:", line.strip())

    # Check pointer position
    print("Position after reading first line:", file.tell())

    # Move pointer to a specific position (e.g., 10th byte)
    file.seek(10)
    print("\nPointer moved to position 10 using seek(10)")
    print("Current position:", file.tell())

    # Read next 10 characters from position 10
    data = file.read(10)
    print("Data from position 10 (10 chars):", data)

    # --------------------------------------------------------
    # Using seek() with different modes
    # --------------------------------------------------------

    # Move pointer relative to current position
    file.seek(5, 1)  # 1 means current position
    print("\nMoved 5 bytes forward from current position")
    print("Current position:", file.tell())

    # Move pointer relative to end of file
    file.seek(-10, 2)  # 2 means from end
    print("\nMoved to 10 bytes before end of file")
    print("Current position:", file.tell())

    # Read remaining content
    data = file.read()
    print("Last 10 bytes of file:", data)


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

"""
Key Points:

1. tell()
   - Returns the current file pointer position (in bytes).
   - Useful to know where you are in a file.

2. seek(offset, whence)
   - Moves the file pointer to a new position.
   - offset: number of bytes to move
   - whence:
        0 -> beginning of file (default)
        1 -> current position
        2 -> end of file

3. Common Usage:
   - seek(0) → go to beginning
   - seek(n) → go to nth byte
   - tell()  → check current position

4. Important:
   - In text mode, behavior of seek() with whence=1 or 2 may vary.
   - For precise control, use binary mode ('rb').

"""