# Explaining about the DocString

def square(n):
    """
    Return the square of a number.

    This docstring is always written immediately under
    the function definition. If it is placed anywhere
    else, Python will not treat it as a docstring.

    Parameters:
        n (int or float): The number to be squared

    Returns:
        int or float: The square of the input number
    """
    return n ** 2


# Call the function
result = square(5)

# Print the returned value
print(result)

# Access and print the docstring
print(square.__doc__)
