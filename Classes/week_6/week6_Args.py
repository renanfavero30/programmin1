#add indefinide nros of parameters

def add (*args)
    #return x + y
    for arg in args:
        total += arg
    return total

a = add(1, 2, 3)
b = add(1, 2, 3, 4)
c = add(1,2, 3, 4, 5, 6)

