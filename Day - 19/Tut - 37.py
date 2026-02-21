# Raising custom errors

# Ask the user to enter a value between 5 and 9
a = int(input("Enter value between 5 and 9: "))

# Check if the entered value is outside the allowed range
if a < 5 or a > 9:
    # Raise an error if the value is not between 5 and 9
    raise ValueError("Value should be between 5 and 9.")

# Ask the user to enter their salary
salary = int(input("Enter your salary: "))

# Check if the salary is not within the valid range (2000 to 5000)
if not 2000 < salary < 5000:
    # Raise an error if the salary is outside the valid range
    raise ValueError("Your salary is not valid.")

# If no error is raised, the inputs are valid
print("All inputs are valid.")