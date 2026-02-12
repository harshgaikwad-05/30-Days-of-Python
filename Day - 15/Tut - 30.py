"""
=========================================================
            RECURSION IN PYTHON - COMPLETE GUIDE
=========================================================

DEFINITION:
Recursion is a programming technique where a function
calls itself to solve a smaller version of the same problem.

IMPORTANT RULE:
Every recursive function MUST have:
1) Base Case      -> Condition where recursion stops
2) Recursive Case -> Function calling itself with smaller input

Without a base case -> Infinite recursion -> Program crashes
"""

# -------------------------------------------------------
# EXAMPLE 1: Simple Countdown
# -------------------------------------------------------

def countdown(n):
    """
    This function prints numbers from n to 1 using recursion.
    
    Base Case:
        If n == 0 → stop recursion.
    
    Recursive Case:
        Print n and call countdown(n-1)
    
    How it works:
        countdown(3)
        -> prints 3
        -> calls countdown(2)
        -> prints 2
        -> calls countdown(1)
        -> prints 1
        -> calls countdown(0) (stops)
    """

    if n == 0:              # Base Case (Stopping condition)
        print("Recursion ends here.")
        return
    
    print("Current value:", n)
    countdown(n - 1)        # Recursive Case


# -------------------------------------------------------
# EXAMPLE 2: Factorial (Classic Recursion Example)
# -------------------------------------------------------

def factorial(n):
    """
    Factorial Definition:
        n! = n × (n-1) × (n-2) × ... × 1
        0! = 1  (Important Base Case)

    Recursive Formula:
        factorial(n) = n * factorial(n-1)

    Base Case:
        if n == 0 → return 1

    Recursive Case:
        return n * factorial(n-1)

    CALL STACK EXPLANATION (factorial(3)):

        factorial(3)
        -> 3 * factorial(2)
            -> 2 * factorial(1)
                -> 1 * factorial(0)
                    -> 1  (Base case reached)

        Now stack resolves:
        1 * 1 = 1
        2 * 1 = 2
        3 * 2 = 6
    """

    if n == 0:                  # Base Case
        return 1
    else:
        return n * factorial(n - 1)   # Recursive Case


# -------------------------------------------------------
# EXAMPLE 3: Sum of First N Natural Numbers
# -------------------------------------------------------

def sum_of_numbers(n):
    """
    Mathematical Idea:
        sum(n) = n + sum(n-1)

    Base Case:
        sum(0) = 0

    Recursive Case:
        return n + sum(n-1)
    """

    if n == 0:          # Base Case
        return 0
    else:
        return n + sum_of_numbers(n - 1)   # Recursive Case


# -------------------------------------------------------
# EXAMPLE 4: Fibonacci Sequence
# -------------------------------------------------------

def fibonacci(n):
    """
    Fibonacci Definition:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2)

    Base Case:
        if n <= 1 → return n

    Recursive Case:
        return fibonacci(n-1) + fibonacci(n-2)

    WARNING:
        This recursive version is slow for large n
        because it repeats many calculations.
    """

    if n <= 1:                  # Base Case
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# -------------------------------------------------------
# COMMON MISTAKE (DO NOT RUN THIS)
# -------------------------------------------------------

"""
Example of Infinite Recursion:

def wrong_function(n):
    return wrong_function(n - 1)

This has:
❌ No base case
Result:
RecursionError: maximum recursion depth exceeded
"""


# -------------------------------------------------------
# MAIN PROGRAM (Testing all functions)
# -------------------------------------------------------

if __name__ == "__main__":

    print("===== COUNTDOWN EXAMPLE =====")
    countdown(5)

    print("\n===== FACTORIAL EXAMPLE =====")
    print("Factorial of 5 is:", factorial(5))

    print("\n===== SUM OF NUMBERS EXAMPLE =====")
    print("Sum of first 5 numbers:", sum_of_numbers(5))

    print("\n===== FIBONACCI EXAMPLE =====")
    print("Fibonacci of 6:", fibonacci(6))


"""
=========================================================
                IMPORTANT CONCEPTS SUMMARY
=========================================================

1) Recursion = Function calling itself
2) Must have:
       - Base Case (stopping condition)
       - Recursive Case (smaller problem)
3) Uses CALL STACK (LIFO - Last In First Out)
4) Too many recursive calls → RecursionError
5) Some recursive problems can also be solved using loops

WHEN TO USE RECURSION:
✔ Tree problems
✔ Divide and conquer algorithms
✔ Backtracking problems
✔ Mathematical definitions (factorial, Fibonacci)

=========================================================
"""