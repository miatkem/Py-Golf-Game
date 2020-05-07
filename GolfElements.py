import contextlib
with contextlib.redirect_stdout(None):
    import pygame
    import pygame.gfxdraw

BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)

class Wall:
    def __init__(self,x,y,width,height,color):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        if type(color) == "string":
            rgb=color[1:len(color)-1].split(',')
            self.color=(int(rgb[0]),int(rgb[1]),int(rgb[2]))
        else:
            self.color=color
    
    def update(self,screen):
        self.draw(screen)
        
    def draw(self,screen):
        pygame.gfxdraw.box(screen, self.rect, self.color)
        pygame.draw.rect(screen,BLACK,self.rect,2)

class Course:
    def __init__(self,name,startLoc,holeLoc,holeSize,par,walls):
        self.name=name
        self.start=startLoc
        self.hole=holeLoc
        self.holeRadius=holeSize
        self.par=par
        self.walls=walls
    
    def update(self,screen):
        for wall in walls:
            wall.update(screen)
        self.draw(screen)
        
    def draw(self, screen):
        pygame.draw.circle(screen, BLACK, hole, holeRadius)
        