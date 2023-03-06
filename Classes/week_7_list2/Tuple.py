a = 12,
print(type(a))

b = (12,)
print(type(a))

d = a+b
c = (12,1,6,9)

print(d)
print(c[1:3])

# can convert to a list

e = list(d)
e[0] = 3
print(e)

c = tuple(b)

x =(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)

#unpacking - not allowed two *var * var
a, *b, c = x # b correspond to the other elements in the midle
print(a,b,c)


