"""
list_methods_explained.py

This file explains ALL built-in Python list methods with examples.
Each method is demonstrated and explained using comments.

Python version: 3.x
"""

# --------------------------------------------------
# Creating a sample list to work with
# --------------------------------------------------
numbers = [1, 2, 3, 4, 5]

# --------------------------------------------------
# 1. append(item)
# Adds an element to the END of the list
# --------------------------------------------------
numbers.append(6)
# Result: [1, 2, 3, 4, 5, 6]


# --------------------------------------------------
# 2. extend(iterable)
# Adds elements of another iterable (list, tuple, set, etc.)
# to the END of the list
# --------------------------------------------------
numbers.extend([7, 8, 9])
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]


# --------------------------------------------------
# 3. insert(index, item)
# Inserts an element at a specific index
# --------------------------------------------------
numbers.insert(0, 0)
# Result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# --------------------------------------------------
# 4. remove(item)
# Removes the FIRST occurrence of the specified value
# Raises ValueError if item not found
# --------------------------------------------------
numbers.remove(9)
# Result: [0, 1, 2, 3, 4, 5, 6, 7, 8]


# --------------------------------------------------
# 5. pop(index)
# Removes and RETURNS the element at the given index
# Default index = -1 (last element)
# --------------------------------------------------
last_item = numbers.pop()
# last_item = 8
# Result: [0, 1, 2, 3, 4, 5, 6, 7]

first_item = numbers.pop(0)
# first_item = 0
# Result: [1, 2, 3, 4, 5, 6, 7]


# --------------------------------------------------
# 6. clear()
# Removes ALL elements from the list
# --------------------------------------------------
temp_list = [1, 2, 3]
temp_list.clear()
# Result: []


# --------------------------------------------------
# 7. index(item, start, end)
# Returns the index of the FIRST occurrence of a value
# Optional start and end range
# Raises ValueError if item not found
# --------------------------------------------------
idx = numbers.index(4)
# idx = 3


# --------------------------------------------------
# 8. count(item)
# Returns the number of times an item appears in the list
# --------------------------------------------------
dup_list = [1, 2, 2, 2, 3, 4]
count_of_2 = dup_list.count(2)
# count_of_2 = 3


# --------------------------------------------------
# 9. sort(key=None, reverse=False)
# Sorts the list IN PLACE (modifies original list)
# --------------------------------------------------
unsorted_list = [5, 3, 1, 4, 2]
unsorted_list.sort()
# Result: [1, 2, 3, 4, 5]

unsorted_list.sort(reverse=True)
# Result: [5, 4, 3, 2, 1]


# --------------------------------------------------
# 10. reverse()
# Reverses the order of the list IN PLACE
# --------------------------------------------------
numbers.reverse()
# Result: [7, 6, 5, 4, 3, 2, 1]


# --------------------------------------------------
# 11. copy()
# Returns a SHALLOW COPY of the list
# --------------------------------------------------
original = [1, 2, 3]
copied = original.copy()
# copied is a new list with same elements


# --------------------------------------------------
# END OF LIST METHODS
# --------------------------------------------------

"""
IMPORTANT NOTES:

1. All list methods modify the list IN PLACE,
   except:
   - copy()
   - index()
   - count()

2. Lists are MUTABLE:
   You can change their content after creation.

3. Use help(list) in Python to see official documentation.

4. Most list methods modify the list in place.
   index(), count(), and copy() do not modify the original list.
"""

print("All list methods demonstrated successfully!")