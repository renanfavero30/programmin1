def print_board(board):
    for row in board[::-1]:
        for element in row:
            print(element, end=" ")
        print()


def initialize_board(num_rows, num_cols):
    rows, cols = 3, 3
    return [["-" for j in range(num_cols)]
            for i in range(num_rows)]

def check_if_winner(board, chip_type):
    # check all rows
    rows, cols = 3,3
    for i in range(rows):
        if board[i][0] == board[i][1] == board[i][2] == chip_type:
            return True
    # check all the columns
    for j in range(cols):
        if board[0][j] == board [1][j] == board [2][j] == chip_type:
            return True

    # check diagonals
    if board[0][0] == board[1][1]== board[2][2] == chip_type:
        return True
    if board[0][2] == board[1][1] == board[2][0] == chip_type:
        return True

    return False
def board_is_full(board):
    for row in board:
        for element in row:
            if element =="-":
                return False
    return True

def available_square(board, row, col):
    return board[row][col] == "-"

def mark_square(board, row, col, chip_type):
    board[row][col] = chip_type

def is_valid(board,row, col):
    if 0 <= row <= 2 and 0<= col <= 2 and board[row][col] == "-":
        return True
    return False


if __name__ == "__main__":
    #board = initialize_board(4,5)
    #print("Player 1: x\nPlayer 2: o\n")
    #print_board(board)

    player = 1
    chip = 'x'

    while True:
        #print(f"Player {player}'s Turn ({chip}): ")
        col = int(input("What would you like the height of the board to be?"))
        row = int(input("What would you like the length of the board to be"))
        input_valid = False
        while input_valid = False:
            if row < 4 or col < 4:
                input_valid = False
                print(f"The board need have more that 4x4 dimension")
                row = int(input("Enter a row number (0, 1, or 2)"))
                col = int(input("Enter a column number (0, 1, or 2)"))
            else:
                return input_valid = True

        mark_square(board, row, col, chip)

        print_board(board)

        # check if there is a winner in th game
        if check_if_winner(board, chip):
            print(f"Player {player} has won!")
            break
        else:
            # no one wins the game yet
            # 1 the game is in progress

            # 2 There is a tie
            if board_is_full(board):
                print("It's a tie")
                break

        # alternate between players
        player = 2 if player == 1 else 1
        chip = 'o' if chip == 'x' else 'x'

