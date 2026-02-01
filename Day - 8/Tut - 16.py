# Creating a Calculator using the Match case

print("\n--- Calculator ---")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choose an option: ")

match choice:
    case "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a + b)

    case "2":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a - b)

    case "3":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a * b)

    case "4":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        match b:
            case 0:
                print("Error: Cannot divide by zero")
            case _:
                print("Result:", a / b)

    case _:
        print("Invalid choice, try again.")
