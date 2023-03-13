import pygame, sys
from constants import *
from tictactoe import *

# pygame template

pygame.init()
pygame.display.set_caption("Tic Tac Toe")
# 1. text drawing: define font
chip_font = pygame.font.Font(None, 400)
font = pygame.font.Font(None, 40)

# initialize game
board = initialize_board()
chip = 'x'
player = 1
game_over = False
winner = 0  # tie


def draw_lines():
    # draw horizontal lines
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen,
                         LINE_COLOR,
                         (0, i * SQUARE_SIZE),
                         (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)

    # draw vertical lines
    for i in range(1, BOARD_COLS):
        pygame.draw.line(screen,
                         LINE_COLOR,
                         (i * SQUARE_SIZE, 0),
                         (SQUARE_SIZE * i, HEIGHT),
                         LINE_WIDTH)


def draw_chips():
    # draw 'x' or 'o' as text in the window/board
    # 2. text drawing: define the text
    chip_x_surf = chip_font.render('x', 0, CROSS_COLOR)
    chip_o_surf = chip_font.render('o', 0, CIRCLE_COLOR)

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'x':
                # 3. text drawing: define the location
                chip_x_rect = chip_x_surf.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2))
                # 4. # text drawing: blit the chip_x_surf onto the screen
                screen.blit(chip_x_surf, chip_x_rect)
            elif board[row][col] == 'o':
                # 3. text drawing: define the location
                chip_o_rect = chip_o_surf.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2))
                # 4. # text drawing: blit the chip_x_surf onto the screen
                screen.blit(chip_o_surf, chip_o_rect)


def draw_game_over_screen(winner):
    screen.fill(BG_COLOR)
    if winner != 0:
        end_text = f"Player {winner} wins!"
    else:
        end_text = "No one wins!"

    end_surf = font.render(end_text, 0, LINE_COLOR)
    end_rect = end_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(end_surf, end_rect)

    restart_text = "Press r to play the game again..."
    restart_surf = font.render(restart_text, 0, LINE_COLOR)
    restart_rect = restart_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 200))
    screen.blit(restart_surf, restart_rect)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)
draw_lines()


while True:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row = y // SQUARE_SIZE
            col = x // SQUARE_SIZE

            if available_square(board, row, col):
                mark_square(board, row, col, chip)

                if check_if_winner(board, chip):
                    game_over = True
                    winner = player
                else:
                    if board_is_full(board):
                        game_over = True
                        winner = 0   # tie

                # alternate between players and chips
                player = 2 if player == 1 else 1
                chip = 'o' if chip == 'x' else 'x'

                draw_chips()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                screen.fill(BG_COLOR)
                draw_lines()
                board = initialize_board()
                game_over = False
                chip = 'x'
                player = 1
                winner = 0

    if game_over:
        pygame.display.update()
        pygame.time.delay(1000)
        draw_game_over_screen(winner)

    pygame.display.update()
