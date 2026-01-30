# Good morning sir using if else:

time = (int(input("Enter The Hour based on your clock between 00:00 to 23:59 : ")))
print("The Hour Right now is : ", time)

if (time >= 6 and time <= 12):
    print("Good Morning Sir")
elif(time >= 13 and time <= 16):
    print("Good Afternoon Sir")
elif(time >= 17 and time <= 19):
    print("Good Evening Sir")
elif(time >= 20 and time <= 23):
    print("Good night sir")
else:
    print("Good Night sir")
