import pygame, sys
from constants import *

# pygame template

pygame.init() #initialize
pygame.display.set_caption(("Tic Tac Toe")) # Name for the game

def draw_lines():
    # draw horizontal lines
    for i in range (1, BOARD_ROWS):
        pygame.draw.line(screen)


screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Set screen
screen.fill(BG_COLOR)

while True: # windows open until something happens
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()