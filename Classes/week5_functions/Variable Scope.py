# Variable declared in one function is only visible inside tht function

def add(x,y):
    add_num = x+y
    return add_num
print(add_num) # give us a error 