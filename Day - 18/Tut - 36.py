# Finally keyword in the Exceptional handling

# try:
#     # risky code
# except SomeException:
#     # handle error
# finally:
#     # always runs

# ================================
# Example 1: Exception Occurs
# ================================

try:
    print("Trying to divide...")
    result = 10 / 0  # This will cause ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
finally:
    # This block ALWAYS runs
    print("Execution completed.")

# ================================
# Example 2: No Exception Occurs
# ================================

try:
    print("Division successful.")
    result = 10 / 2
except ZeroDivisionError:
    print("Error occurred.")
finally:
    print("Execution completed.")