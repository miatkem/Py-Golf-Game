import contextlib
with contextlib.redirect_stdout(None):
    import pygame
    import pygame.gfxdraw
from UIElements import Button
from UIUtilities import MouseHandler

GREEN = pygame.Color(22,91,19)
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)
BROWN = pygame.Color(139,69,19)
DARK_YELLOW = pygame.Color(249,166,2)

class Menu:
    def __init__(self,dimensions):
        self.state="idle"
        self.golfFlagImg = pygame.image.load('golfFlag.png')
        self.golfFlagImg = pygame.transform.scale(self.golfFlagImg, (600, 450))
        self.display_width=dimensions[0]
        self.display_height=dimensions[1]
        center = (self.display_width/2, self.display_height/2)
        self.playButton=Button(center[0]-150,center[1]+100,300,50,GREEN,"Play",32)
        self.buildButton=Button(center[0]-150,center[1]+200,300,50,GREEN,"Build",32)
        self.settingsButton=Button(center[0]-150,center[1]+300,300,50,GREEN,"Settings",32)
            
    def update(self, screen, mouseHandler):
        self.draw(screen)
        self.playButton.update(screen,mouseHandler)
        self.buildButton.update(screen,mouseHandler)
        self.settingsButton.update(screen,mouseHandler)  
        if self.playButton.clicked:
            self.state="goto play"
        elif self.buildButton.clicked:
            self.state="goto build"
        elif self.settingsButton.clicked:
            self.state="goto setting"        
        
    def draw(self, screen):
        pygame.gfxdraw.box(screen,pygame.Rect(0,0,self.display_width,self.display_height), DARK_YELLOW)
        screen.blit(self.golfFlagImg, (200,-15))