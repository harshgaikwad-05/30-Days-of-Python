"""
Dictionary Methods in Python
This program demonstrates commonly used dictionary methods:
update(), clear(), pop(), popitem(), and del
"""

# ---------------------------------------------
# 1️⃣ Creating Dictionaries
# ---------------------------------------------

# Dictionary ep1
ep1 = {10: 45, 11: 56, 12: 78, 13: 89}

# Dictionary ep2
ep2 = {15: 67, 17: 74, 19: 94}


# ---------------------------------------------
# 2️⃣ update() Method
# ---------------------------------------------
# update() merges another dictionary into the current dictionary.
# If keys are the same, values will be overwritten.

ep1.update(ep2)

print("After update():")
print(ep1)  
# Output: {10: 45, 11: 56, 12: 78, 13: 89, 15: 67, 17: 74, 19: 94}


# ---------------------------------------------
# 3️⃣ clear() Method
# ---------------------------------------------
# clear() removes all items from the dictionary.

ep3 = {10: 45, 11: 56, 12: 78, 13: 89}

ep3.clear()

print("\nAfter clear():")
print(ep3)  
# Output: {}


# ---------------------------------------------
# 4️⃣ Creating an Empty Dictionary
# ---------------------------------------------
# You can create an empty dictionary using {}

empt = {}

print("\nEmpty Dictionary:")
print(empt)  
# Output: {}


# ---------------------------------------------
# 5️⃣ pop() Method
# ---------------------------------------------
# pop(key) removes the specified key and returns its value.

ep1.pop(10)

print("\nAfter pop(10):")
print(ep1)
# Removes key 10 and its value


# ---------------------------------------------
# 6️⃣ popitem() Method
# ---------------------------------------------
# popitem() removes and returns the last inserted key-value pair.
# (Dictionaries maintain insertion order in Python 3.7+)

ep1.popitem()

print("\nAfter popitem():")
print(ep1)


# ---------------------------------------------
# 7️⃣ del Statement
# ---------------------------------------------
# del is used to completely delete a dictionary.

del ep3

# If you try to print ep3 now, it will cause an error
# because the dictionary no longer exists.

# print(ep3)  # This would raise NameError