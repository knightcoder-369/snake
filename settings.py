import pygame
from sys import exit #it will help us to exit the game
from os.path import join #join will help to import images


#we are trying to make pixels in our case it is 80 pixels
CELL_SIZE=80 #pixels
ROWS=10
COLS=16
WINDOW_WIDTH=COLS*CELL_SIZE
WINDOW_HEIGHT=ROWS*CELL_SIZE #800 pixels tall

#COLRS
lIGHT_GREEN='#aad751'
DARK_GREEN='#a2d149'

#start pos
START_LENGTH=3
START_ROW=ROWS//2
START_COL=START_LENGTH+2

#SHADOW
SHADOW_SIZE=pygame.Vector2(4,4)
SHADOW_OPACITY=50