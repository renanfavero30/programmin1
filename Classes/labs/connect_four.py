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
    for row in range(0, len(board)):
        if board[row][col] == '-':
            board[row][col] = chip_type
            return board, row, col

def board_is_full(board):
    for row in board:
        for chip in row:
            if chip == "-":
                return False
    return True
    # at specific col
    # loop through all the rows at the specific col
    # if board[i][col] == '-', return i
    #pass

# row: row index returned from insert_chip
# col: col index entered by the user in the main logic


def check_if_winner(board, col, row, chip_type):
    #print("we are checking the winner func")
    #1. fix the row, loop throught all the columns
        # check whether there are four consecutive chip_type (same logic)
    #2. fix the column, loop through all the rows
        # check whether there are four consecutive chip_type

    '''
      0 1 2 3 
    0 - - - -
    1 - - - -
    2 - - - -
    3 - - - -
    
    checking if a row has 4 consecutive marks
    if row = 2
    
    if board[2][j] == board[2][j+1] == ...
        return true
    '''
    # print('col: ', col)
    # print('row: ', row)
    # print('chip type: ', chip_type)
    horizontal_win=False
    for j in range(len(board)-3):
        j += 1
        # we are now in the araray of THE row we put the mark on
        # go through the array and check if we have 4 consecutive marks
        horizontal_win = board[-j][row] == board[-(j+1)][row] == board[-(j+2)][row] == board[-(j+3)][row] == chip_type
        #print('horizontal: ',board[-j][row],board[-(j+1)][row], board[-(j+2)][row] ,board[-(j+3)][row], horizontal_win )
        if horizontal_win:
            return True

    vertical_win = False
    for i in range(len(board[0])-3):
        i += 1
        vertical_win = board[col][-i] == board[col][-(i+1)] == board[col][-(i+2)] == board[col][-(i+3)] == chip_type
        #print('vertical: ', board[col][-i], board[col][-(i+1)] , board[col][-(i+2)] , board[col][-(i+3)], vertical_win)
        if vertical_win:
            return True

        '''
    for i in range(len(board)-3):
        print('TEST ROW WIN')
        if board[row][i] == board[row][i +1] == board[row][i+2] == board[row][i+3] == chip_type:
            return True
    # check all the row
    for j in range(len(board[0])-3):
        print(len(board[0]))
        print('TEST COL WIN')
        if board[j][col] == board[j+1][col] == board[j+3][col] == chip_type:
            return True
    return False
        '''



if __name__ == "__main__":
    # board = initialize_board(4,5)
    # print("Player 1: x\nPlayer 2: o\n")
    # print_board(board)

    player = 1
    chip_type = 'x'
    game_finished = False
    while not game_finished:
        # print(f"Player {player}'s Turn ({chip}): ")
        num_rows = int(input("What would you like the height of the board to be?"))
        num_cols = int(input("What would you like the length of the board to be?"))
        input_valid = False
        while input_valid == False:
            if num_cols < 4 or num_rows < 4:
                input_valid = False
                print(f"The board need have more that 4x4 dimension")
                num_cols = int(input("What would you like the height of the board to be?"))
                num_rows = int(input("What would you like the length of the board to be?"))
            else:
                input_valid = True

        #Show the board
        board = initialize_board(num_rows, num_cols)
        print_board(board)
        print()
        print("Player 1: x")
        print("Player 2: o")

        game_continue = True

        # player choose an option
        while game_continue:
            col = int(input(f"Player {player}: Which column would you like to choose?"))

            board, row, col = insert_chip(board, col, chip_type)
            print_board(board)
            print()
            if check_if_winner(board, row, col, chip_type):
                print(f"Player {player} won the game!")
                game_continue = False
                game_finished = True
                break
            else:
                if board_is_full(board):
                    print("Draw. Nobody wins.")
                    game_continue = False
                    game_finished = True
                    break
            # alternating between players
            player = 2 if player == 1 else 1
            chip_type = 'o' if chip_type == 'x' else 'x'


