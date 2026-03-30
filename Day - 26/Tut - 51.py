"""
===========================================================
Difference between '==' and 'is' in Python
===========================================================

'=='  → Checks VALUE equality (Are the contents the same?)
'is'  → Checks IDENTITY (Are both variables pointing to the same object in memory?)

===========================================================
"""

# -------------------------------
# Example 1: Basic integers
# -------------------------------

a = 10
b = 10

# '==' checks if values are equal
print("a == b:", a == b)   # True → values are the same

# 'is' checks if both refer to same memory location
print("a is b:", a is b)   # True (Python may reuse small integers)


# -------------------------------
# Example 2: Lists (IMPORTANT)
# -------------------------------

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print("\nlist1 == list2:", list1 == list2)
# True → values inside lists are the same

print("list1 is list2:", list1 is list2)
# False → different objects in memory


# -------------------------------
# Example 3: Same reference
# -------------------------------

list3 = list1   # both point to SAME object

print("\nlist1 == list3:", list1 == list3)
# True → values are same

print("list1 is list3:", list1 is list3)
# True → same memory location


# -------------------------------
# Example 4: Strings
# -------------------------------

str1 = "hello"
str2 = "hello"

print("\nstr1 == str2:", str1 == str2)
# True → same value

print("str1 is str2:", str1 is str2)
# Usually True (Python may reuse strings, but not guaranteed)


# -------------------------------
# Example 5: None comparison (BEST PRACTICE)
# -------------------------------

x = None

# Correct way
if x is None:
    print("\nx is None → Correct way to check None")

# Avoid this
if x == None:
    print("x == None → Works, but NOT recommended")


# -------------------------------
# FINAL SUMMARY
# -------------------------------

"""
Use '==' when you want to compare VALUES.

Use 'is' when you want to compare OBJECT IDENTITY
(i.e., whether both variables refer to the SAME object).

Common Rule:
- Numbers/Strings → usually use '=='
- Objects (lists, dicts) → use '==' for content comparison
- None → ALWAYS use 'is'
"""