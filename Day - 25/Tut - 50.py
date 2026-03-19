"""
===========================================================
        MAP, FILTER, AND REDUCE IN PYTHON
===========================================================

This file provides a complete guide to:
1. map()
2. filter()
3. functools.reduce()

Each section includes:
- Definition
- Syntax
- Examples
- Comparison with list comprehensions
- Best practices

===========================================================
"""

# =========================================================
# 1. MAP FUNCTION
# =========================================================

"""
map() applies a function to every item in an iterable
and returns a map object (iterator).

SYNTAX:
    map(function, iterable)

You usually convert the result into a list:
    list(map(...))
"""

print("----- MAP EXAMPLES -----")

# Example 1: Square numbers
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x * x

mapped_result = map(square, numbers)
print("Squares using map:", list(mapped_result))

# Example 2: Using lambda
mapped_lambda = map(lambda x: x * x, numbers)
print("Squares using lambda:", list(mapped_lambda))

# Example 3: Multiple iterables
a = [1, 2, 3]
b = [4, 5, 6]

sum_result = map(lambda x, y: x + y, a, b)
print("Sum of two lists:", list(sum_result))


# =========================================================
# MAP vs LIST COMPREHENSION
# =========================================================

"""
List comprehension is often more readable in Python.
"""

lc_result = [x * x for x in numbers]
print("List comprehension result:", lc_result)


# =========================================================
# 2. FILTER FUNCTION
# =========================================================

"""
filter() filters elements based on a condition (function returns True/False)

SYNTAX:
    filter(function, iterable)
"""

print("\n----- FILTER EXAMPLES -----")

# Example 1: Filter even numbers
def is_even(x):
    return x % 2 == 0

filtered_result = filter(is_even, numbers)
print("Even numbers:", list(filtered_result))

# Example 2: Using lambda
filtered_lambda = filter(lambda x: x % 2 == 0, numbers)
print("Even numbers (lambda):", list(filtered_lambda))

# Example 3: Filter strings
names = ["Alice", "Bob", "Charlie", "David"]

long_names = filter(lambda name: len(name) > 3, names)
print("Names longer than 3 characters:", list(long_names))


# =========================================================
# FILTER vs LIST COMPREHENSION
# =========================================================

lc_filter = [x for x in numbers if x % 2 == 0]
print("List comprehension (filter):", lc_filter)


# =========================================================
# 3. REDUCE FUNCTION
# =========================================================

"""
reduce() applies a function cumulatively to items in an iterable.

It is part of functools module.

SYNTAX:
    from functools import reduce
    reduce(function, iterable)

It reduces the iterable into a single value.
"""

from functools import reduce

print("\n----- REDUCE EXAMPLES -----")

# Example 1: Sum of all numbers
numbers = [1, 2, 3, 4, 5]

sum_result = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce:", sum_result)

# Example 2: Product of all numbers
product_result = reduce(lambda x, y: x * y, numbers)
print("Product using reduce:", product_result)

# Example 3: Find maximum
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print("Maximum value:", max_value)


# =========================================================
# REDUCE vs BUILT-IN FUNCTIONS
# =========================================================

"""
In many cases, built-in functions are preferred:
"""

print("\nBuilt-in sum:", sum(numbers))
print("Built-in max:", max(numbers))


# =========================================================
# COMBINING MAP, FILTER, REDUCE
# =========================================================

print("\n----- COMBINED EXAMPLE -----")

# Goal:
# 1. Filter even numbers
# 2. Square them
# 3. Sum the result

numbers = [1, 2, 3, 4, 5, 6]

result = reduce(
    lambda x, y: x + y,
    map(lambda x: x * x,
        filter(lambda x: x % 2 == 0, numbers))
)

print("Final combined result:", result)


# =========================================================
# BEST PRACTICES
# =========================================================

"""
1. Use map() when:
   - You are applying a function to all elements

2. Use filter() when:
   - You need to select elements based on condition

3. Use reduce() when:
   - You need a single aggregated result

4. Prefer list comprehensions for readability:
   - Pythonic and easier to understand

5. Use built-in functions when available:
   - sum(), max(), min(), etc.

6. Avoid overusing lambda:
   - Use named functions if logic is complex
"""


# =========================================================
# SUMMARY
# =========================================================

"""
map()    → Transform each element
filter() → Select elements
reduce() → Combine elements into one result
"""