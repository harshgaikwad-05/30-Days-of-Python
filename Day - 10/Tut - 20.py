# Function to calculate the mean
def calculate_gmean(a, b):
    mean = (a * b) / (a + b)
    print(f"Mean of {a} and {b} is: {mean}")


# Function to check which number is greater
def is_greater(a, b):
    if a > b:
        print("First number is greater.")
    else:
        print("Second number is greater or equal.")


# Function to check which number is lesser
def is_lesser(a, b):
    pass
# It is a placeholder statement used when Python requires a block of code, but you don’t want to write anything yet.
# Work in progress — will complete later.

# First set of values
a = 9
b = 8
calculate_gmean(a, b)
is_greater(a, b)

print()  # blank line for readability

# Second set of values
c = 10
d = 12
calculate_gmean(c, d)
is_greater(c, d)