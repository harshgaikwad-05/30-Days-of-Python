# Everything about import statement
# The import is the statement and the math here is the module that is to be imported
import math
# from math import sqrt, pi (We can get a specific function we want this will only add the sqrt==square and pi value)
# from math import * (This will add all the functions that are inside the math)
# import math as m (as is used to rename the function so that we dont have to write the full function name.)

result = math.floor(4.2334)
print(result)    # The result will be 4.

square = math.sqrt(9)
print(square)    # The result will be 3.0

'''
DIR function print(dir(math))
Python has a built-in function called dir
that you can use to view the names of all the functions
and variables defined in the module
'''