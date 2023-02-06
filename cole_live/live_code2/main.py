#Live Code 2
# remove the gray part ( 3 number iquals)

# input colors number
red = int(input())
green = int(input())
blue = int(input())

numbers = [ red, green, blue]

smallest = red
for n in numbers:
    if smallest > green:
        smallest = green
    elif smallest > blue:
        smallest = blue

print((red-smallest), end=" ")
print((green-smallest), end=" ")
print((blue-smallest))