# Basic Syntax for Match case

# match value:
#     case option1:
#         # code
#     case option2:
#         # code
#     case _:
#         # default (like else)

"""
match_case_example.py

This file explains Python's match-case statement.
Python version required: 3.10 or above
"""

# Ask the user for a number
choice = int(input("Enter a number (1-3): "))

# Match-case checks the value of 'choice'
match choice:
    case 1:
        print("You chose Pizza 🍕")
    case 2:
        print("You chose Burger 🍔")
    case 3:
        print("You chose Pasta 🍝")
    case _:
        print("Invalid choice ❌")

"""
How it works:
1. Python checks the value of 'choice'
2. It compares it with each case
3. When a match is found, that block runs
4. If no match is found, case _ runs
"""