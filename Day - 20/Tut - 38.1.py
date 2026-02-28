# ✅ 1. Simple Calculator Using if-elif-else

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", num1 + num2)

elif op == "-":
    print("Result:", num1 - num2)

elif op == "*":
    print("Result:", num1 * num2)

elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error! Cannot divide by zero.")

else:
    print("Invalid operator!")

# ✅ 2. Simple Calculator Using Short-Hand (Ternary Operator)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

result = (
    num1 + num2 if op == "+" else
    num1 - num2 if op == "-" else
    num1 * num2 if op == "*" else
    num1 / num2 if op == "/" and num2 != 0 else
    "Error!"
)

print("Result:", result)