import contextlib
with contextlib.redirect_stdout(None):
    import pygame
    import pygame.gfxdraw
from UIElements import Button, Text, ScrollButtonList
from UIUtilities import MouseHandler
from GolfElements import Course, Wall

GREEN = pygame.Color(22,91,19)
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)
BROWN = pygame.Color(139,69,19)
DARK_YELLOW = pygame.Color(249,166,2)

class LevelSelection:
    def __init__(self,dimensions):
        self.state="idle"
        self.display_width=dimensions[0]
        self.display_height=dimensions[1]        
        self.levels=self.loadLevels(self.loadLevelNames())
        center = (self.display_width/2, self.display_height/2)
        self.levelsLabel = Text(center[0],10,"Pick a level:", pygame.font.Font(pygame.font.get_default_font(), 32))
        self.levelButtons=[]
        print(self.levels)
        for level in self.levels:
            text = str(level.name) + " Par: " + str(level.par)
            self.levelButtons.append(Button(200,100,600,100,GREEN,text,32))
        self.buttonList = ScrollButtonList(200,100,625,540, self.levelButtons)
        self.backButton = Button(50,650,100,50,GREEN,"BACK")
    
    def update(self, screen, mouseHandler):
        self.draw(screen)
        self.buttonList.update(screen, mouseHandler)
        pygame.gfxdraw.box(screen,pygame.Rect(0,0,self.display_width,90), DARK_YELLOW)
        pygame.gfxdraw.box(screen,pygame.Rect(0,675,self.display_width,300), DARK_YELLOW)        
        self.backButton.update(screen, mouseHandler)
        self.levelsLabel.update(screen)
        
        if self.buttonList.selectedButton != None:
            self.state="playLevel " + self.buttonList.selectedButton.text.split()[0]
        elif self.backButton.clicked:
            self.state="goto menu"
        
    def draw(self, screen):
        pygame.gfxdraw.box(screen,pygame.Rect(0,0,self.display_width,self.display_height), DARK_YELLOW)
        
    def loadLevelNames(self):
        file = open("LevelNames.txt")
        lines = [line.rstrip('\n') for line in file]
        return lines
    
    def loadLevels(self,levelNames):
        levels=[]
        for name in levelNames:
            file = open(name + ".txt")
            lines = [line.rstrip('\n') for line in file]
            for line in lines:
                walls=[]
                start=(0,0)
                hole=(self.display_width,self.display_height)
                holeSize=0
                par=0
                words=line.split()
                if words[0]=="wall":
                    walls.append(Wall(int(words[1]),int(words[2]),int(words[3]),int(words[4]),words[5]))
                if words[0]=="par":
                    par=int(words[1])    
                if words[0]=="start":
                    start=(int(words[1]),int(words[2]))
                if words[0]=="hole_size":
                    holeSize=int(words[1])
                if words[0]=="hole":
                    hole=(int(words[1]),int(words[2]))
            levels.append(Course(name,start,hole,holeSize,par,walls))
        return levels    