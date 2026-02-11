# ============================================
# simple_sets.py
# A simple explanation of sets in Python
# ============================================

# -------------------------------
# 1. What is a Set?
# -------------------------------
# A set is a collection of unique values.
# "Unique" means no duplicate values are allowed.
# Sets are unordered, meaning the items do not have a fixed position.

# -------------------------------
# 2. Creating a Set
# -------------------------------

# Creating a set using curly braces {}
numbers = {1, 2, 3, 4}

print("Original set:", numbers)

# If we add duplicate values, Python automatically removes them
duplicate_numbers = {1, 2, 2, 3, 3, 4}
print("Set with duplicates removed:", duplicate_numbers)

# -------------------------------
# 3. Creating an Empty Set
# -------------------------------

# IMPORTANT:
# {} creates an empty dictionary, NOT a set.
# To create an empty set, use set()

empty_set = set()
print("Empty set:", empty_set)

# -------------------------------
# 4. Adding Elements to a Set
# -------------------------------

# We use add() to insert a new value
numbers.add(5)
print("After adding 5:", numbers)

# If we add a duplicate, nothing changes
numbers.add(5)
print("After adding 5 again:", numbers)

# -------------------------------
# 5. Removing Elements from a Set
# -------------------------------

# remove() deletes a specific value
numbers.remove(3)
print("After removing 3:", numbers)

# -------------------------------
# 6. Checking if an Item Exists
# -------------------------------

# We use the 'in' keyword to check membership

print("Is 2 in the set?", 2 in numbers)
print("Is 10 in the set?", 10 in numbers)

# -------------------------------
# 7. Looping Through a Set
# -------------------------------

# We can use a for loop to go through all elements
print("Looping through the set:")
for item in numbers:
    print(item)

# -------------------------------
# 8. Important Characteristics of Sets
# -------------------------------

# 1. No duplicate values allowed
# 2. Unordered (items do not have index numbers)
# 3. Mutable (we can add or remove items)
# 4. Items must be immutable (numbers, strings, tuples allowed)
#    Lists are NOT allowed inside sets

# Example of valid set
valid_set = {1, "hello", (1, 2)}
print("Valid set:", valid_set)

# Example of invalid set (uncommenting below line will cause an error)
# invalid_set = {1, [2, 3]}  # Lists cannot be inside sets

print("End of simple sets example.")
