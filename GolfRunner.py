import math, random
from PIL import Image
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
    import pygame.gfxdraw
from UIElements import Button
from UIUtilities import MouseHandler
from MenuState import Menu
from LevelSelectionState import LevelSelection
        
#create display width height
display_width = 1000
display_height = 750

#game states
MENU_SCREEN = 0
LEVEL_SELECTION = 1
LEVEL_BUILDER = 2
GAME_SCREEN = 3


#initialize pygame environement
pygame.init()
systemDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Golf')
clock = pygame.time.Clock()
GREEN = pygame.Color(22,91,19)
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)
BROWN = pygame.Color(139,69,19)
DARK_YELLOW = pygame.Color(249,166,2)

#load
systemDisplay.fill(WHITE)
pygame.display.update()

mouseHandler=MouseHandler()

#flags
crashed = False
gameState = Menu((display_width,display_height))

#system loop
while not crashed:
    
    mouseHandler.update()
    gameState.update(pygame.display.get_surface(),mouseHandler) 
    
    if gameState.state.split()[0] == "goto":
        if gameState.state.split()[1] == "build":
            gameState=Builder(mouseHandler)
        elif gameState.state.split()[1] == "play":       
            gameState=LevelSelection((display_width,display_height))
        elif gameState.state.split()[1] == "menu":
            gameState=Menu((display_width,display_height))
        elif gameState.state.split()[1] == "settings":
            gameState=Settings(mouseHandler)
    if gameState.state.split()[0] == "playLevel":
        print("lets play " + gameState.state.split()[1])
        gameState=PlayLevel((display_width,display_height))
    elif gameState.state.split()[0] == "quit":
        quit()
    
    #event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    
    #update display and tick clocks
    pygame.display.update()
    clock.tick(100)    