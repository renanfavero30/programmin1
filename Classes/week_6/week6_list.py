# Overview of buit-in types
# numeric (number)
# sequence (ordered collection of objects)
a = [1, 2, 3, 4] # List = mutable (you can olug or change values inside)
b = (1, 2, 3, 4) # Tuple: imutable
# b[0] = 10 -> give us an error
c = range(0, 5) # range

# container
d = {1, 2,1000} # set - there is no index in the elements inside - not a sequence
print(d)

e = {"0": 0, "F": 15} # Dictionary: key-> value pair

hex_digit = "F"
print(e[hex_digit])

f = False * 2
print(f)

#messages = "line 1"\ # two lines together
    #"line 2"

nro =100
welcome_nro = "welcome to COP" +str(nro)
print(welcome_nro)
welcome = "Welcome"
w = welcome
print (w)

print(len(welcome))

print(a[0], a[1])

print(a[2:0]) # print everything after 0,1,2 digits

# a[1] = 'a' # string is immutable - inside the variable 1
print(a)

#but you can change the variable
a= "hello"

# ASCII Code
# convert
digit ="b"
print(ord(digit))

def hex_char_code(digit):
    # digit = "E" is 4 greater than "A" return 14
    digit = digit.lower() # E -> e

    return ord(digit) - ord('a') + 10

print (hex_char_code('A'))


my_list = ["a", "b", "c", "d"]

print(my_list[-1], my_list[-3])
print(my_list[0:3])
print(f" inverse order for the index number using -1{my_list[:-1]}") # from begining until -1
print(f"using -3{my_list[-3:]}") # from -3 until end
print(my_list[:]) #select all

print(my_list[0:4:2]) #jump 2
print(my_list[::-1]) # reverse the list

g = [2,3,4,5,1]
print(g[-1]) # give you back and element
print(g[-1:]) # give you a list

# Change element
g[-1] = 6
print(g)

# error: a[-1:] = 100 -> Sintax error
g[-1:] = [100] # assigment to slicing is an interable
print(g)

g[1:] = [1000, 2000]
print(g)

g[1:] = "python"
print(g)

g[1:] = ["python", "test"]
print(g)

# To remove

g.pop() # remove the last element
print(g)

# Removing more elements
g[1:] =[]
print(g)

# Append add elements at end of the list
g.append(199)
print(g)

# add one element at time in the end of the list
g.extend([100, 101, 102])
print(g)

# Include element in a specific position, such as in the index 3
g.insert(3,"inserted")
print(g)

# remove one element in the list by the element name
g.remove("inserted")
print(g)

# remove one element by index
g.pop(1)
print(g)

# Sort a list
g.sort()
print(g)

# Reverse - we ca not rever string because is unmutable

hex ="1a2345"
ls = list(hex)
print(ls)
ls.reverse()
print(ls)

# To clear
ls.clear()
ls[:] = []

# List comprehensions
a = [1,2,3]
# b = [ 2, 4, 6, 8]
b = a * 2 # just repet 2 times the same list
print(b)

b = []
for i in a:
    b.append(i*2)
print(b)

# Same result
b = [i * 2 for i in a]
print(b)

# map function
def my_map(function, a_list):
    return [function(i) for i in a_list]

square = lambda x: x*x
print(my_map(square, [1,2,3,4]))
