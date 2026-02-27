"""
===========================================
        SHORT-HAND IF-ELSE IN PYTHON
===========================================

This file explains:
1. One-line if statement
2. Short-hand if-else (Ternary Operator)
3. Comparison with normal if-else

===========================================
"""

# ===========================================
# 1️⃣ ONE-LINE IF STATEMENT
# ===========================================

# Syntax:
# if condition: statement

print("----- Example 1: One-line if statement -----")

age = 18

# If age is greater than or equal to 18,
# print "You are an adult"
if age >= 18:
    print("You are an adult")

print()  # Blank line for better output formatting


# ===========================================
# 2️⃣ SHORT-HAND IF-ELSE (TERNARY OPERATOR)
# ===========================================

# Syntax:
# value_if_true if condition else value_if_false

print("----- Example 2: Short-hand if-else -----")

age = 16

# Assign value based on condition
status = "Adult" if age >= 18 else "Minor"

print("Age:", age)
print("Status:", status)

print()


# ===========================================
# 3️⃣ NORMAL IF-ELSE (FOR COMPARISON)
# ===========================================

print("----- Example 3: Normal if-else -----")

age = 16

if age >= 18:
    status = "Adult"
else:
    status = "Minor"

print("Age:", age)
print("Status:", status)

print()


# ===========================================
# 4️⃣ PRACTICAL EXAMPLE – EVEN OR ODD
# ===========================================

print("----- Example 4: Even or Odd Checker -----")

number = 7

# If number is divisible by 2 → Even
# Otherwise → Odd
result = "Even" if number % 2 == 0 else "Odd"

print("Number:", number)
print("Result:", result)

# ===========================================
# END OF PROGRAM
# ===========================================