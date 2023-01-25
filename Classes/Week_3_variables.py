number = input("enter an integer:")
print(type(number))
number = int(number)
print(type(number))
print(id(number))

# 3 importat informations : value, type and id

# can be in the same line or in diferents lines the inputs variables
num_bananas, num_monkeys, a, b = 10, 6, 3, 2
num_monkeys = 6

print (f' There are {num_monkeys}'
       f'little monkeys jumping on the bed ... \n'
       f' One fell of and bumped his head')

num_monkeys = 5
print('Now just' + str(num_monkeys) +'...')

# we can start  variable name with _ or letter

_number = 1
number = 1
number3 = 1
#number! = 3 # doesnt work
#  can't be a key word (False, None, ...)
#num_trees = input("how many trees:")

# PEP 8 conventions
  # File/modulos names should have short and ALL low case
  #class name should use UpperCamelCass

class ApplePhone:
    pass

  # Variables and methods names should use low case
    # function:
def hello_world_cop_3502c():
    pass #pass doesnt do anything here

# All caps for constants with underscores between words
RED_COLOR = (255, 0, 0)

# In Python, everything is an objects
# Programs manipulate values
# Each value has a certain data type

value = input()
print (type(value))
print(type(float(value)))

# Bool variables
game_over = False
game_continue = True


# Divided
20% 7 = 6# Modulo
20//7 = 2 # integer as result
20/7 = # float as a result

a = 3
a = a * 3
a *= 3 # compound operations

a = a % 5
a %= 5

# TEST
a = 15
b = 5
print(a/b)

c 12.0
print(c//b)