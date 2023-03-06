#Set is a unordered collection of unique

a= {1,2,3}
b=set([100,2,1])

#c=a+b #print(c) - ERROr

c = a.union(b)
print((c))

# to see the diference:
h= a.difference(b)
print(a,b,h)

e = a.intersection(b)
print(a,b,e)

# Sets are mutable

a ={1,2,3} # set
d = set()
print(d, type(d))

e = {} # empty dictionary
print(e, type(e))
e_set = {"q": 2, "a": 3} #dictionary

e.add(3) # add one element to my_set
e.update({a,5,3,8}) # add elements to my_set
