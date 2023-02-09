def square(x):
    return x* x

a = square(3)
b = (lambda x: x*x)(4) #means that I will use one time and I will not use anymoroe in my code
            #4: 4 * 4 = 16
print(b)

# we can assign a function as object even when it has a anonymous_function
square_number = lambda x: x* x
print(square_number(3))

add = lambda x, y: x + y
print(add(3, 12))

# another way to call the function:
print((lambda x, y: x + y)(3,10))