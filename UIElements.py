import contextlib
with contextlib.redirect_stdout(None):
    import pygame
    import pygame.gfxdraw
from UIUtilities import MouseHandler
GREEN = pygame.Color(22,91,19)
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)
BROWN = pygame.Color(139,69,19)
DARK_YELLOW = pygame.Color(249,166,2)

class Button:
    def __init__(self, x, y, width, height, color, text="", fontSize = 12):
        self.x=x
        self.y=y
        self.width = width
        self.height = height
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        self.mouseIsOver = False
        self.clicked=False
        self.color = color
        self.hoverColor = (color[0]-15,color[1]-15,color[2]-15)
        self.currentColor = color
        self.text=text
        self.fontSize = fontSize
        self.font = pygame.font.Font(pygame.font.get_default_font(), self.fontSize)
        self.border = (BLACK, 4)
        self.render()
    
    def render(self):
        self.renderedText = self.font.render(self.text, True, (0xff, 0xff, 0xff))
        self.text_rect = self.renderedText.get_rect()
        self.text_rect.center = self.rect.center          
    
    def mouseOver(self, mouseHandler):
        if mouseHandler.mouseLocation[0] > self.x and mouseHandler.mouseLocation[0] < self.x+self.width and mouseHandler.mouseLocation[1] > self.y and mouseHandler.mouseLocation[1] < self.y+self.height:
            self.mouseIsOver=True
            self.currentColor=self.hoverColor
            if mouseHandler.mouseReleased:
                self.clicked=True
            return True
        self.currentColor=self.color
        self.mouseIsOver=False
        return False
    
    def update(self, screen, mouseHandler):
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        self.render()
        if self.clicked:
            self.clicked=False
        self.mouseOver(mouseHandler)
        self.draw(screen)
        
    def draw(self, screen):
        pygame.gfxdraw.box(screen, self.rect, self.currentColor)      
        screen.blit(self.renderedText, self.text_rect)
        pygame.draw.rect(screen,self.border[0],self.rect,self.border[1])
        
class ScrollButtonList:
    def __init__(self,x,y,width, height, buttons, spacing=10):
        self.x=x
        self.y=y
        self.width = width
        self.height = height
        self.buttons = buttons
        self.spacing= spacing
        
        
        self.totalHeight=0
        for b in self.buttons:
            self.totalHeight+=b.height+self.spacing
        self.totalHeight-=self.spacing
        
        if self.totalHeight > self.height:
            self.scrollable = True
        else:
            self.scrollable = False
        
        yOffset=self.y
        for i in range(len(self.buttons)):
            self.buttons[i].x=self.x
            self.buttons[i].y=yOffset
            yOffset=self.buttons[i].y+self.buttons[i].height+10
            
        self.scrollTab = Button(self.x+self.width-10,self.y,10,20,WHITE)
        self.scrollTabRatio = (self.totalHeight-self.height)/self.height
        self.scrollTabLastLocation = self.scrollTab.y
        self.selectedButton = None
        self.scrolling = False
    
    def addButton(self, button):
        self.buttons.append(button)
    
    def update(self,screen, mouseHandler):
        self.draw(screen)
        
        self.scrollTab.update(screen,mouseHandler)
        if self.scrollTab.mouseOver(mouseHandler):
            self.scrolling = True
        if mouseHandler.mouseHold and self.scrolling:
            if mouseHandler.mouseLocation[1] > self.y + self.height:
                self.scrollTab.y= self.y + self.height
            elif  mouseHandler.mouseLocation[1] < self.y:
                self.scrollTab.y= self.y
            else:
                self.scrollTab.y=mouseHandler.mouseLocation[1] 
        else:
            self.scrolling = False        
        
        if self.scrollTab.y != self.scrollTabLastLocation:
            scrollTabLocation = self.scrollTab.y-self.scrollTabLastLocation
            offset = scrollTabLocation*self.scrollTabRatio         
            for i in range(len(self.buttons)):          
                self.buttons[i].y=self.buttons[i].y-offset
                self.scrollTabLastLocation=self.scrollTab.y 
        for i in range(len(self.buttons)): 
            self.buttons[i].update(screen,mouseHandler)
            if self.buttons[i].clicked:
                self.selectedButton = self.buttons[i]  
        
    def draw(self,screen):
        pygame.draw.line(screen, BLACK, (self.x+self.width-5,self.y),(self.x+self.width-5,self.y+self.height+20))
        

class Text:
    def __init__(self,x,y,text,font):
        self.x=x
        self.y=y
        self.font=font
        self.text=text
        self.isCenter=False
        self.render()
    
    def render(self):
        self.renderedText = self.font.render(self.text, True, (0xff, 0xff, 0xff))
        self.text_rect = self.renderedText.get_rect()
        if self.isCenter:
            self.text_rect.center = (self.x,self.y)
    
    def update(self, screen):
        self.draw(screen)
        
    def draw(self, screen):
        screen.blit(self.renderedText, self.text_rect)
