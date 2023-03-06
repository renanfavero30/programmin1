#command-line arguments are values entered by a user when running a program from a command line

import sys # to use the command lines

for args in sys.argv:
    print(args)

# Functions Arguments
## Arguments passed by objectes reference which is alos know as pass-by-assignment:
# *If the object is immutable (string or integer), the passing is like pass by value
# * if the object is mutable (list), the passing is like pass-by-reference

def plus(x):
    x[0] = x[0] + 1

y = [1,2,3]
plus(y)

print(y)