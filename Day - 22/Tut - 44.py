"""
========================================
        PYTHON OS MODULE EXAMPLES
========================================

The 'os' module in Python allows us to interact with
the operating system. It helps in working with files,
directories, environment variables, and system info.

Author: Example for Students
"""

# Import the OS module
import os


# ----------------------------------------
# 1. Get Current Working Directory
# ----------------------------------------
print("\n1. Current Working Directory")
current_directory = os.getcwd()
print("Current Directory:", current_directory)


# ----------------------------------------
# 2. List Files and Folders
# ----------------------------------------
print("\n2. Files and Folders in Current Directory")
files = os.listdir()
print(files)


# ----------------------------------------
# 3. Create a New Directory
# ----------------------------------------
print("\n3. Creating a New Folder")
folder_name = "demo_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created:", folder_name)
else:
    print("Folder already exists")


# ----------------------------------------
# 4. Rename a Folder
# ----------------------------------------
print("\n4. Renaming the Folder")

old_name = "demo_folder"
new_name = "renamed_folder"

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print("Folder renamed to:", new_name)
else:
    print("Folder not found")


# ----------------------------------------
# 5. Check if File or Folder Exists
# ----------------------------------------
print("\n5. Checking if Folder Exists")

if os.path.exists(new_name):
    print("Yes,", new_name, "exists")
else:
    print("Folder does not exist")


# ----------------------------------------
# 6. Join File Paths
# ----------------------------------------
print("\n6. Joining Paths")

path = os.path.join("folder", "file.txt")
print("Joined Path:", path)


# ----------------------------------------
# 7. Get Operating System Name
# ----------------------------------------
print("\n7. Operating System Name")

print("OS Name:", os.name)
# nt -> Windows
# posix -> Linux/Mac


# ----------------------------------------
# 8. Get Environment Variable
# ----------------------------------------
print("\n8. Environment Variable Example")

path_variable = os.environ.get("PATH")
print("PATH Variable:", path_variable[:100], "...")  # printing first 100 chars


# ----------------------------------------
# 9. Remove Directory
# ----------------------------------------
print("\n9. Removing Folder")

if os.path.exists(new_name):
    os.rmdir(new_name)
    print("Folder removed:", new_name)
else:
    print("Folder not found")

print("\nProgram Finished Successfully")