import contextlib
with contextlib.redirect_stdout(None):
    import pygame
    import pygame.gfxdraw

class MouseHandler():
    def __init__(self):
        self.mouseHold=False
        self.mouseReleased=False
        self.mouseLocation = (0,0)
        self.clickLocation = (0,0)
    def update(self):
        left_pressed, middle_pressed, right_pressed =  pygame.mouse.get_pressed()
        self.mouseLocation=pygame.mouse.get_pos()
        #mouse event handling 
        if left_pressed: #mouse being pressed/held
            if self.mouseHold == False:
                self.mouseHold=True
                self.clickLocation=pygame.mouse.get_pos()
        elif self.mouseReleased:
            self.mouseReleased =False
        elif self.mouseHold == True and not left_pressed: #mouse released
            self.mouseReleased = True
            self.mouseHold = False