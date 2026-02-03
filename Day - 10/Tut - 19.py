# ============================================
# Learning the Break and Continue Statements
# ============================================

# --------------------------------------------
# BREAK STATEMENT
# --------------------------------------------
# The break statement is used to stop a loop
# completely. Once Python sees `break`,
# it immediately exits the loop.

for i in range(1, 13):
    print("5 x", i, "=", 5 * i)
    if i == 10:
        break

# Even though the range goes up to 12,
# the loop stops when i == 10.


# --------------------------------------------
# CONTINUE STATEMENT
# --------------------------------------------
# The continue statement skips the current
# iteration and moves to the next one.
# The loop itself does NOT stop.

for i in range(1, 13):
    if i == 9:
        continue
    print("2 x", i, "=", 2 * i)

# The value 9 is skipped, but the loop continues.


# --------------------------------------------
# SIMPLE EXAMPLE OF BREAK
# --------------------------------------------
for number in range(1, 6):
    if number == 3:
        break
    print(number)

# Step-by-step:
# number = 1 → printed
# number = 2 → printed
# number = 3 → break → loop stops


# --------------------------------------------
# SIMPLE EXAMPLE OF CONTINUE
# --------------------------------------------
for number in range(1, 6):
    if number == 3:
        continue
    print(number)

# Step-by-step:
# number = 1 → printed
# number = 2 → printed
# number = 3 → skipped
# number = 4 → printed
# number = 5 → printed