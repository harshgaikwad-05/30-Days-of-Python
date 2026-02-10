# =========================================
# F-STRINGS IN PYTHON (Formatted String Literals)
# =========================================

# -----------------------------------------
# 1. Old way: Using .format()
# -----------------------------------------

name = "Julia"
country = "Deutschland"

# We create a string with placeholders {}
letter = "Hey, my name is {} and I am from {}"

# The values are inserted in order using .format()
print(letter.format(name, country))


# -----------------------------------------
# 2. New & recommended way: Using f-strings
# -----------------------------------------

# f-strings start with the letter 'f' before the quotes
# Variables can be placed directly inside {} and are evaluated automatically
print(f"Hello, my name is {name} and I am from {country}")


# -----------------------------------------
# 3. Printing curly braces literally
# -----------------------------------------

# To print { or } in an f-string, use double braces {{ }}
print(f"This shows variable names, not values: {{name}} and {{country}}")


# -----------------------------------------
# 4. Using f-strings with numbers (floats)
# -----------------------------------------

price = 49.1582

# :.2f means:
# .  -> decimal point
# 2  -> number of digits after the decimal
# f  -> floating-point number
formatted_price = f"This t-shirt costs only {price:.2f} dollars"

print(formatted_price)


# -----------------------------------------
# 5. Expressions inside f-strings
# -----------------------------------------

# You can even do math directly inside an f-string
quantity = 3
print(f"Total price for {quantity} items is {price * quantity:.2f} dollars")


# -----------------------------------------
# 6. Why f-strings are great
# -----------------------------------------
# - Cleaner and easier to read
# - Faster than .format()
# - Allows expressions and formatting inline
# - Introduced in Python 3.6+