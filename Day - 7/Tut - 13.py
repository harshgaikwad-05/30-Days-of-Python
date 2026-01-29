# Learning about the If-Else statements

print("There are 4 types of If-else Statements.")
print("- If Statement")
print("- If-else Statement")
print("- If-elif-else Statement")
print("- If-nested-else Statement")

print("-" * 40)

# If-Else Statement

age = int(input("Enter Your age: "))

# Conditional Operatos are : >, <, <=, >=, ==, !=
print(age>18)
print(age<18)
print(age>=18)
print(age<=18)
print(age==18)
print(age!=18)

print("-" * 40)

print("Your age is : ", age)

if (age>18):
    print("You can drive")
else:
    print("You cannot drive")

print("-" * 40)

# If-elif-else Statement

dl = int(input("Do you have Driving License: Yes=1 or No=0 or Expired=2: "))

if (dl==1):
    print("Good You can Drive Your car")
elif (dl==0):
    print("Get Your License first")
else:
    print("Renew Your License")

# If-nested-else Statement

print("-" * 40)

num = 18
if (num<0):
    print("Number is Negative")
elif(num>0):
    if(num <= 10):
        print("Number comes between 1-10")
    elif(num > 10 and num <=20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
    print("Num is Positive")
else:
    print("The Number is Zero")