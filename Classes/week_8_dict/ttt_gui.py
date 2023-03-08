import pygame, sys
from constants import *
from tictactoe import *

# pygame template

pygame.init() #initialize
pygame.display.set_caption("Tic Tac Toe") # Name for the game

#1. text drawing: define font
chip_font = pygame.font.Font(None, 400)


# initialialize board
board = initialize_board()
mark_square(board, 0, 0, "x")


def draw_lines():
    # draw horizontal lines
    for row in range (1, BOARD_ROWS):
        pygame.draw.line(screen,
                         LINE_COLOR,
                         (0, row * SQUARE_SIZE),(WIDTH, row * SQUARE_SIZE), LINE_WIDTH)

    # draw vertical lines
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR,
                         (col * SQUARE_SIZE, 0), #start points
                         (SQUARE_SIZE * col, HEIGHT), # end points
                         LINE_WIDTH)


def draw_chips():
    # draw x or o as text in the windows/board
    for row in range(0, BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'x':
                # 2. text drawing: define the text
                chip_x_surf = chip_font.render("x", 0, CROSS_COLOR)
                # 3. text drawing: define the location
                chip_x_rect = chip_x_surf.get_rect(center = (col *SQUARE_SIZE + SQUARE_SIZE //2, row *SQUARE_SIZE + SQUARE_SIZE //2))
                # 4. text drawing:  blit the chip_x_surf into the screen
                screen.blit(chip_x_surf, chip_x_rect)
            elif board[row][col] == "o":
                # 2. text drawing: define the text
                chip_o_surf = chip_font.render("o", 0, CIRCLE_COLOR)
                # 3. text drawing: define the location
                chip_o_rect = chip_o_surf.get_rect(center = (col *SQUARE_SIZE + SQUARE_SIZE //2, row *SQUARE_SIZE + SQUARE_SIZE //2))
                # 4. text drawing:  blit the chip_x_surf into the screen
                screen.blit(chip_o_surf, chip_o_rect)


screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Set screen
screen.fill(BG_COLOR)
draw_lines()
draw_chips()


while True: # windows open until something happens
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()