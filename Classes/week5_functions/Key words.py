def add( x, y, z):
    return x + y + z


print(add(3, y =7, z=4)) # if mixed position arg need to be in a righ position first
#print(x = 1, 4, 5 ) # Error sintaxe - key arg always came last!!!!

# Using default values
def add2( x, y, z=9): # DEFAULT VALUES ALWAYS CAME LAST
    return x + y + z
print(add2(1,2))
