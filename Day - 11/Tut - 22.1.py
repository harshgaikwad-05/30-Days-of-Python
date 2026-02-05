# =====================================
# Python List Comprehension - Basics
# =====================================

# List comprehension is a short way
# to create a new list from an existing list


# -------------------------------------
# Example 1: Normal loop vs comprehension
# -------------------------------------

numbers = [1, 2, 3, 4]

# Normal way
new_list = []
for x in numbers:
    new_list.append(x * 2)

print("Normal loop result:")
print(new_list)

# List comprehension way
comp_list = [x * 2 for x in numbers]

print("\nList comprehension result:")
print(comp_list)


# -------------------------------------
# Example 2: Squaring numbers
# -------------------------------------

numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print("\nSquares of numbers:")
print(squares)


# -------------------------------------
# Example 3: Using condition (if)
# -------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [x for x in numbers if x % 2 == 0]

print("\nEven numbers only:")
print(even_numbers)


# -------------------------------------
# Example 4: Double only even numbers
# -------------------------------------

double_even = [x * 2 for x in numbers if x % 2 == 0]

print("\nDouble of even numbers:")
print(double_even)


# -------------------------------------
# Example 5: Working with strings
# -------------------------------------

names = ["john", "alice", "bob"]

capital_names = [name.upper() for name in names]

print("\nCapitalized names:")
print(capital_names)


# -------------------------------------
# Summary
# -------------------------------------
# Structure:
# [expression for item in iterable if condition]
#
# List comprehension helps you:
# - Write clean code
# - Reduce lines
# - Create new lists easily