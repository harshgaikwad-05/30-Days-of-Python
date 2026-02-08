# ==================================================
# Updating Tuples in Python
# ==================================================
# Tuples are immutable, meaning their elements cannot be changed directly.
# To add, remove, or modify elements, we must:
# 1. Convert the tuple into a list
# 2. Perform the required operations
# 3. Convert the list back into a tuple

# Original tuple
countries = ("Spain", "Germany", "India", "England", "Italy")
print("Original tuple:", countries)

# Convert tuple to list
temp = list(countries)

# Add a new country to the list
temp.append("Russia")
print("After adding an element:", temp)

# Remove the element at index 3 ("England")
temp.pop(3)
print("After removing an element:", temp)

# Modify the element at index 2
temp[2] = "Finland"
print("After modifying an element:", temp)

# Convert the list back to a tuple
countries = tuple(temp)
print("Updated tuple:", countries)


# ==================================================
# Tuple Concatenation
# ==================================================
# Tuple concatenation is the process of combining two or more tuples into
# a single tuple using the '+' operator. The original tuples remain unchanged
# because tuples are immutable.

# First tuple
fruits = ("Orange", "Apple", "Kiwi", "Mango", "Pineapple")

# Second tuple
fruits2 = ("Banana", "Strawberries", "Watermelon")

# Concatenating two tuples
allfruits = fruits + fruits2

# Printing the result
print("All fruits:", allfruits)


# ==================================================
# Tuple count() Method
# ==================================================
# The count() method is used to find the number of times a specified value
# appears in a tuple. It returns an integer representing the total occurrences
# of that value.

# Creating a tuple
tuple1 = (0, 1, 2, 3, 1, 3, 5, 4, 2, 1, 6)

# Counting how many times 1 appears in the tuple
count_1 = tuple1.count(1)

# Printing the result
print("Count of 1 in tuple1:", count_1)


# ==================================================
# Tuple index() Method
# ==================================================
# The index() method is used to find the position of the first occurrence
# of a specified value in a tuple.
# If the value is not found, it raises a ValueError.

# Syntax:
# tuple.index(element, start, end)
# element → value to search for
# start   → starting index of the search
# end     → ending index of the search (not included)

# Finding the index of 1 between index 5 and 10
idx = tuple1.index(1, 5, 10)

# Printing the result
print("Index of 1 between index 5 and 10:", idx)


# ==================================================
# len() Function
# ==================================================
# The len() function is used to find the number of elements in a tuple.

length_tuple = len(tuple1)
print("The length of tuple1:", length_tuple)
