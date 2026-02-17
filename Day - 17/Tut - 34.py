# ✅ Example 1: Basic for-else (No break)
def example_basic_for_else():
    """
    This function demonstrates a simple for-else loop.
    The else block runs because there is NO break statement.
    """
    
    for i in range(5):
        print("Value of i:", i)
    else:
        # This runs after the loop finishes normally
        print("Loop completed successfully. No break occurred.")
        

# Calling the function
example_basic_for_else()

# ✅ Example 2: Loop Over a List (No break)
def example_list_without_break():
    """
    This function loops through a list.
    Since there is no break statement, 
    the else block will execute.
    """
    
    numbers = [1, 2, 3, 4]
    
    for num in numbers:
        print("Number:", num)
    else:
        print("Loop finished successfully!")
        

# Calling the function
example_list_without_break()

# ❌ Example 3: Using break (Else Will NOT Run)
def example_with_break():
    """
    This function demonstrates that 
    the else block does NOT execute 
    if the loop is stopped using break.
    """
    
    numbers = [1, 2, 3, 4]
    
    for num in numbers:
        if num == 3:
            print("Found 3! Breaking the loop.")
            break  # Loop stops here
        print("Number:", num)
    else:
        # This will NOT execute because of break
        print("Loop finished successfully!")
        

# Calling the function
example_with_break()