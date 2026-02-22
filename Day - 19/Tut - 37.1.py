print("Simple Calculator")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    if num2 == 0:
        raise ValueError("You cannot divide by zero!")
    print("Result:", num1 / num2)

else:
    raise ValueError("Invalid operator! Use +, -, *, or /")