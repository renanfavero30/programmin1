
# Arbitrary numbers of key args
def add(**kwargs):
    total = 0
    for key, value in kwargs.items():
        # key=a, value=1
        total += value
    return total

print(add(a=1, b=2, c=3))
print(add(a=3, x=4, y=2, z=2))
