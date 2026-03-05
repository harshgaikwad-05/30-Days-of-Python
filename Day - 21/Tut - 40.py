# This is how we use the simple method to get the index and the Values stored.
john_friends = ["Lisa", "Selena", "Hokong", "Taylor"]

for i in range(len(john_friends)):
    print(i,john_friends[i])

# This is how we can use the enumerate funtion easily to get the same index and value.

lisa_friends = ["John", "Selena", "Hokong", "Taylor"]

for index, friends_of_lisa in enumerate(lisa_friends):
    print(index, friends_of_lisa)

# for index, value in enumerate(iterable):
#     # code to execute

# A proper syntax of enumerate is:
# for variable_1(index)-to store the Index value, variable_2(var_name)-Variable name to store the values "in" enumerate(iterable)-list, tuple or string
    # Code to execute "print(variable_1, variable_2)"