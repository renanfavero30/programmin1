def print_board(board):
    for row in board[::-1]:
        for element in row:
            print(element, end=" ")
        print()

def initialize_board(num_rows, num_cols):
    return[["-" for j in range(num_cols)]
        for i in range(num_rows)]

def insert_chip(board, col, chip_type): # col is the index
    # starting from row 0 of the board
    # at specific col
    # loop through all the rows at the specific col
    # if board[i][col] == '-', return i
    pass

# row: row index returned from insert_chip
# col: col index entered by the user in the main logic


def check_if_winner(board, col, row, chip_type):
    #1. fix the row, loop throught all the columns
        # check whether there are four consecutive chip_type (same logic)
    #2. fix the column, loop through all the rows
        # check whether there are four consecutive chip_type

    pass


if__name__ == "__main__":
    board = initializa_board(4, 5)
    print_board(board)

    board[0][0] = "x"
    print_board(board)

