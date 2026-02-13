# Create two sample sets for demonstration
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Initial sets:")
print("set1:", set1)
print("set2:", set2)
print()


# add(element): Add an element to set1
set1.add(7)
print("After set1.add(7):", set1)
print()


# clear(): Remove all elements from the set
set1_copy = set1.copy()  # avoid modifying original
set1_copy.clear()
print("After set1_copy.clear():", set1_copy)
print()


# copy(): Create a shallow copy of the set
set1_copy2 = set1.copy()
print("set1_copy2 (copy of set1):", set1_copy2)
print()


# difference(*others): Elements in set1 but not in set2
diff = set1.difference(set2)
print("set1.difference(set2):", diff)
print()


# difference_update(*others): Remove elements found in other sets
set1_copy3 = set1.copy()
set1_copy3.difference_update(set2)
print("After set1_copy3.difference_update(set2):", set1_copy3)
print()


# discard(element): Remove element if it exists (no error if missing)
set1.discard(7)
print("After set1.discard(7):", set1)
print()


# intersection(*others): Elements common to both sets
inter = set1.intersection(set2)
print("set1.intersection(set2):", inter)
print()


# intersection_update(*others): Keep only common elements
set1_copy4 = set1.copy()
set1_copy4.intersection_update(set2)
print("After set1_copy4.intersection_update(set2):", set1_copy4)
print()


# isdisjoint(other): True if sets have no common elements
disjoint = set1.isdisjoint(set2)
print("set1.isdisjoint(set2):", disjoint)
print()


# issubset(other): True if set1 is contained in set2
subset = set1.issubset(set2)
print("set1.issubset(set2):", subset)
print()


# issuperset(other): True if set1 contains all elements of set2
superset = set1.issuperset(set2)
print("set1.issuperset(set2):", superset)
print()


# pop(): Remove and return an arbitrary element
popped = set1.pop()
print("Popped element from set1:", popped)
print("set1 after pop():", set1)
print()


# remove(element): Remove specific element (error if not found)
set1.add(8)
set1.remove(8)
print("After set1.remove(8):", set1)
print()


# symmetric_difference(other): Elements in either set but not both
sym_diff = set1.symmetric_difference(set2)
print("set1.symmetric_difference(set2):", sym_diff)
print()


# symmetric_difference_update(other): Update with symmetric difference
set1_copy5 = set1.copy()
set1_copy5.symmetric_difference_update(set2)
print("After set1_copy5.symmetric_difference_update(set2):", set1_copy5)
print()


# union(*others): All unique elements from both sets
uni = set1.union(set2)
print("set1.union(set2):", uni)
print()


# update(*others): Add elements from other sets
set1_copy6 = set1.copy()
set1_copy6.update(set2)
print("After set1_copy6.update(set2):", set1_copy6)
print()


# ==============================
# OPERATOR EQUIVALENTS
# ==============================

# | : Union operator
print("set1 | set2:", set1 | set2)

# & : Intersection operator
print("set1 & set2:", set1 & set2)

# - : Difference operator
print("set1 - set2:", set1 - set2)

# ^ : Symmetric difference operator
print("set1 ^ set2:", set1 ^ set2)
print()


# |= : Update with union
set_op = set1.copy()
set_op |= set2
print("After set_op |= set2:", set_op)

# &= : Update with intersection
set_op = set1.copy()
set_op &= set2
print("After set_op &= set2:", set_op)

# -= : Update with difference
set_op = set1.copy()
set_op -= set2
print("After set_op -= set2:", set_op)

# ^= : Update with symmetric difference
set_op = set1.copy()
set_op ^= set2
print("After set_op ^= set2:", set_op)
print()


# ==============================
# BUILT-IN FUNCTIONS FOR SETS
# ==============================

# len(set): Number of elements
print("len(set1):", len(set1))

# min(set): Smallest element
if set1:
    print("min(set1):", min(set1))

# max(set): Largest element
if set1:
    print("max(set1):", max(set1))

# sum(set): Sum of numeric elements
if set1:
    print("sum(set1):", sum(set1))
print()


# Final state of set1
print("Final set1:", set1)
