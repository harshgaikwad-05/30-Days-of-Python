"""
Python Function Arguments – Complete Example File

Topics Covered:
1. Required Arguments
2. Default Arguments
3. Keyword Arguments
4. Variable Length Arguments (*args)
5. Keyword Variable Length Arguments (**kwargs)
"""

# --------------------------------------------------
# 1. REQUIRED ARGUMENTS
# --------------------------------------------------
# These arguments MUST be passed when calling the function

def multiply(a, b):
    # a and b are required arguments
    print("Multiplication:", a * b)

multiply(4, 5)
# multiply(4)  # ❌ Uncommenting this will cause an error


# --------------------------------------------------
# 2. DEFAULT ARGUMENTS
# --------------------------------------------------
# Default values are used if no argument is passed

def average(a=9, b=5):
    # a and b have default values
    print("The average is:", (a + b) / 2)

average()        # Uses default values
average(4, 6)    # Overrides both defaults
average(10)      # a = 10, b = 5 (default)


# --------------------------------------------------
# 3. KEYWORD ARGUMENTS
# --------------------------------------------------
# Arguments are passed using parameter names
# Order does NOT matter

def student(name, age):
    print("Student Name:", name)
    print("Student Age:", age)

student(age=20, name="Rahul")


# --------------------------------------------------
# 4. VARIABLE LENGTH ARGUMENTS (*args)
# --------------------------------------------------
# Used when the number of arguments is unknown
# *args stores values as a tuple

def total_sum(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print("Total Sum:", sum)

total_sum(1, 2, 3)
total_sum(10, 20, 30, 40)


# --------------------------------------------------
# 5. KEYWORD VARIABLE LENGTH ARGUMENTS (**kwargs)
# --------------------------------------------------
# **kwargs stores values as a dictionary (key-value pairs)

def student_details(**info):
    for key, value in info.items():
        print(key, ":", value)

student_details(name="Amit", age=22, course="Python")


# --------------------------------------------------
# 6. COMBINING ALL TYPES OF ARGUMENTS
# --------------------------------------------------
# Order: Required → Default → *args → **kwargs

def full_demo(a, b=10, *args, **kwargs):
    print("Required Argument a:", a)
    print("Default Argument b:", b)
    print("Variable Length args:", args)
    print("Keyword Variable kwargs:", kwargs)

full_demo(5, 20, 1, 2, 3, name="Neha", city="Delhi")

# [] → List → Changeable  
# () → Tuple → Fixed  
# {} → Set / Dict → Unique or Key:Value  
# "" → String → Text
