# Exception Handling 

# Ask the user to enter a number
a = input("Enter a Number: ")

# Print a heading for the multiplication table
print(f"\nThe Multiplication Table of {a} is:\n")

# Try block: Code that might cause an error
try:
    # Loop from 1 to 10
    for i in range(1, 11):
        # Convert input to integer and print multiplication
        print(f"{int(a)} X {i} = {int(a) * i}")

# Except block: Runs if something goes wrong in try block
except:
    print("Invalid Input! Please enter a valid number.")

# These lines will run whether error happens or not
print("\nSome lines of code")
print("End of the Program")

# try:
#     # Code that might cause a problem
# except:
#     # Code that runs if a problem happens