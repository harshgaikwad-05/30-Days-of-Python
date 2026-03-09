# example.py

# A simple function
def greet(name):
    """
    This function prints a greeting message.
    It can be reused if this file is imported as a module.
    """
    print(f"Hello, {name}!")


# This code runs every time the file is executed OR imported
print("This line runs whenever the file is loaded.")


# Python automatically sets a special variable called __name__
# If this file is run directly:
#     __name__ == "__main__"
# If this file is imported into another file:
#     __name__ == "example"  (the module name)


# This block runs ONLY when the file is executed directly
if __name__ == "__main__":
    
    # This part will NOT run if the file is imported
    print("This file is being run directly.")

    # Calling the function
    greet("Alice")