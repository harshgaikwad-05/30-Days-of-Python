"""
File: local_vs_global.py
Author: Example
Description:
    This file demonstrates the concept of Local and Global Variables in Python.
    It includes multiple examples explaining scope rules, usage, and the 'global' keyword.
"""

# -----------------------------------------------------------
# GLOBAL VARIABLE
# -----------------------------------------------------------
# A global variable is defined outside all functions.
# It can be accessed from anywhere in the file.

global_var = "I am a global variable"


# -----------------------------------------------------------
# Example 1: Accessing a global variable inside a function
# -----------------------------------------------------------
def access_global():
    """
    This function accesses a global variable.
    Since we are only reading it, we do NOT need the 'global' keyword.
    """
    print("Inside access_global():", global_var)


# -----------------------------------------------------------
# Example 2: Local variable inside a function
# -----------------------------------------------------------
def local_variable_example():
    """
    A local variable is defined inside a function.
    It can only be accessed inside that function.
    """
    local_var = "I am a local variable"
    print("Inside local_variable_example():", local_var)


# -----------------------------------------------------------
# Example 3: Local variable vs global variable with same name
# -----------------------------------------------------------
name = "Global Name"

def variable_shadowing():
    """
    If a local variable has the same name as a global variable,
    the local variable 'shadows' (overrides) the global variable
    inside that function.
    """
    name = "Local Name"
    print("Inside variable_shadowing():", name)


# -----------------------------------------------------------
# Example 4: Modifying a global variable using 'global'
# -----------------------------------------------------------
counter = 0

def modify_global():
    """
    To modify a global variable inside a function,
    we must declare it using the 'global' keyword.
    """
    global counter
    counter += 1
    print("Inside modify_global(): counter =", counter)


# -----------------------------------------------------------
# Example 5: Nested function and scope
# -----------------------------------------------------------
def outer_function():
    """
    Demonstrates variable scope in nested functions.
    """
    outer_var = "I belong to outer_function"

    def inner_function():
        # inner_function can access outer_var
        print("Inside inner_function():", outer_var)

    inner_function()


# -----------------------------------------------------------
# MAIN EXECUTION
# -----------------------------------------------------------
if __name__ == "__main__":

    print("----- Global Variable Access -----")
    access_global()

    print("\n----- Local Variable Example -----")
    local_variable_example()

    print("\n----- Variable Shadowing -----")
    variable_shadowing()
    print("Outside function:", name)

    print("\n----- Modifying Global Variable -----")
    print("Before function call: counter =", counter)
    modify_global()
    print("After function call: counter =", counter)

    print("\n----- Nested Function Scope -----")
    outer_function()


# -----------------------------------------------------------
# Key Points Summary
# -----------------------------------------------------------
"""
1. Local Variable
   - Declared inside a function.
   - Accessible only within that function.

2. Global Variable
   - Declared outside all functions.
   - Accessible throughout the program.

3. 'global' Keyword
   - Used when you want to modify a global variable inside a function.

4. Variable Shadowing
   - A local variable with the same name as a global variable overrides it
     inside the function scope.

5. Scope Levels (LEGB Rule)
   - L : Local
   - E : Enclosing
   - G : Global
   - B : Built-in
"""