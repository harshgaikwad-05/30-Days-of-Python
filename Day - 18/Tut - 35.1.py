# Exception Handling

# Syntax for the Try and Except
# try:
#     # risky code
# except ErrorType:
#     # what to do if error happens

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("You cannot divide by zero!")

except ValueError:
    print("Please enter valid numbers!")
