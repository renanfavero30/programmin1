my_list = [
    [1,2,3], # row x columns
    [4,5,6]
    ]

#2D list -> list of list

# Access elements:
print(my_list[1][2])
print(my_list[-1][-2])

# To dimensional list

board1 = [
    [ "-", "-","-","-","-","-"],
    [ "-", "-","-","-","-","-"],
    [ "-", "-","-","-","-","-"],
    [ "-", "-","-","-","-","-"],
    [ "-", "-","-","-","-","-"]
]

rows = len(board1)
cols = len(board1[0])

print(rows, cols)

rows = 4
cols = 5

board = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append("-")
    board.append(row)

for row in board:
    for col in row:
        print(col, end="")
    print()


