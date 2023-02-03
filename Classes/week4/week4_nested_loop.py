# week 4 Nested loop

#for i in range (2,10,2):
 #   print(i)

width, height = input("what will be box size?").split()

for i in range (0, int(height)):
    for j in range(0, int(width)):
        print("*", end="")
    print()

print("second box")

for i in range( 0, 4):
    for j in range(0,8):
        print("*", end="")
    print()