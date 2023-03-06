# Associates key with value. Keys must be of an immutable type

my_dict = {'name': 'Jack', 'age': 26}

a= {(1,2): 1, (3,4):2} # Tuple are immutable so we can use as a key
print(a)

dic = {"a":1, "b":2}
print(dic["a"])

# to update value
dic["b"] = 24
print(dic)

# How include value
dic["c"] = 3
print(dic)

# delete
del dic["a"]
print(dic)

#Key is unique
dic["b"] = 4 # just update the b value

dic["b"] +=2
print(dic)

#Dictionary iteration
def magic(**kwargs): #acess all k values
    for key, value in kwargs.item():
        print(key, value)

for a_key, b_value in dic.items():
    print("a", a_key, "b", b_value)

for akey in dic.keys():
    print(akey)

for b_value in dic.values():
    print(b_value)



print(dic.get("c", 0)) # 0 defoult value - no probel

