nested = [0]
original = [nested,1]
print(original)

nested[0] = "zero"
print(original)

original[0][0] = [2]
print(original)

# Shallow copy always refernece to the same list nested

# Deep copy
import copy

original = [[0], 1]
shallow = original[:]
deep = copy.deepcopy(original)


shallow[0][0]=2
print(original, shallow)

deep[0][0] = 3
print(original, deep)