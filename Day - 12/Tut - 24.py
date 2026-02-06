# ============================
# TUPLES IN PYTHON - BASICS
# ============================

# A tuple is a collection of values
# It can store multiple items in a single variable
# Tuples are ORDERED and IMMUTABLE

# ORDERED:
# - Items have a fixed position (index)
# - The order never changes

# IMMUTABLE:
# - Once a tuple is created, you CANNOT change its values
# - You cannot add, remove, or replace items


# ----------------------------
# CREATING A TUPLE
# ----------------------------

# A tuple is created using parentheses ()
numbers = (1, 2, 3, 4)

# Tuples can store different data types
mixed = (1, "hello", 3.5, True)

# You can also create a tuple without parentheses
letters = "a", "b", "c"

# A tuple with only ONE item MUST have a comma
single_item = (5,)
# Without the comma, Python thinks it's just a number
not_a_tuple = (5)


# ----------------------------
# ACCESSING TUPLE ITEMS
# ----------------------------

# Tuples use indexing (starts from 0)
colors = ("red", "green", "blue")

first_color = colors[0]    # "red"
second_color = colors[1]   # "green"
third_color = colors[2]    # "blue"

# Negative indexing starts from the end
last_color = colors[-1]    # "blue"


# ----------------------------
# TUPLE LENGTH
# ----------------------------

# You can check how many items are in a tuple
count = len(colors)


# ----------------------------
# LOOPING THROUGH A TUPLE
# ----------------------------

# You can loop through a tuple using a for loop
for color in colors:
    print(color)


# ----------------------------
# IMMUTABILITY EXAMPLE
# ----------------------------

# This will cause an ERROR because tuples cannot be changed
# colors[0] = "yellow"


# ----------------------------
# NESTED TUPLES
# ----------------------------

# A tuple can contain another tuple
nested = (1, 2, (3, 4))

# Accessing items inside nested tuples
inner_value = nested[2][0]  # 3


# ----------------------------
# TUPLE VS LIST (CONCEPT ONLY)
# ----------------------------

# LIST:
# - Uses []
# - Can be changed
# - Slower, but flexible

# TUPLE:
# - Uses ()
# - Cannot be changed
# - Faster and safer for fixed data


# ----------------------------
# WHEN TO USE TUPLES
# ----------------------------

# Use tuples when:
# - Data should not change
# - You want to protect values
# - You want better performance


# ----------------------------
# END OF TUPLE BASICS
# ----------------------------