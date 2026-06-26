import sys
import pygame
import camera

class Camera_System:
    def __init__(self, screen, x, y, next_camera):
        self.screen = screen
        #self.minimap_image = pygame.image.load("")
        self.cameras = [1 , 2, 3, 4, 5, 6]
        self.minimap_x = x
        self.minimap_y = y
        self.next_camera = next_camera
        for i in range(6):

    def Draw_Minimap(self):
        self.screen.blit(self.minimap_image, (self.minimap_x, self.minimap_y))
    def Camera_On_or_Off(self):
        
    def Switch_Camera(self):
        