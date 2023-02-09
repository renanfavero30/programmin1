#Python functions can be passed as arguments

def say_hello(func, first, last):
    message = func(first, last)
    print(message)

#HOF
# 1 + 2 + 3 + 4 + 5 + 6 + ...
# 1^2 + 2^2 + 3^2 + 4 ^2...
# 1^3 + 2^4 + 3^3 + 4 ^3...
# 8 / (1*3) + 8 / (5*7) + 8 / (9*11) + ...

def identity(i):
    return i
def square(i):
    return i * 1

def cube(i):
    return i ** 3

def pi_sum(i):
    return 8 / ((4 * i-3)) * ((4 * i-1))

def sum_nums(mystery, x):
    i, total = 1,0
    while i <= x:
        total = total + mystery(i)
        i += 1
    return total

print(sum_nums(square,4))
