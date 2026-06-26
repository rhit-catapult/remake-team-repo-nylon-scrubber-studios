import pygame
import camera_system
import office_module
import project

class Button:
    def __init__(self, screen,x,y,image,function):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.function = function
    def draw(self):
        if self.in_camera == True:
            return
        self.screen.blit(self.image,(self.x,self.y))

    #determine if button was pushed
    def is_pressed(self,pos):
        posx = pos[0]
        posy = pos[1]
        return (self.x < posx < self.width and self.y < posy < self.height)