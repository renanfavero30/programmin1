my_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(my_list[2][1])

for row in my_list:
    for item in row:
        print(item,end=" ")
    print()