import sys
import pygame
import os
import counselor_module
import button_module

class Camera:

    #creates a camera
    def __init__(self, screen: pygame.Surface, camera_image,x,y):
        self.screen = screen
        self.camera_image = pygame.image.load(camera_image)
        self.counselors_in_camera = []
        self.folder = []
        self.button = button_module.Buttons(screen,x,y,"images/button_test.png")
        camera_num = 0

    #loads the image files into a variable
    # def load_images(self):
    #     self.ethan = pygame.image.load(self.folder[2])
    #     self.carp = pygame.image.load(self.folder[1])
    #     self.jj = pygame.image.load(self.folder[3])
    #     self.andrew = pygame.image.load(self.folder[0])

    #draws the camera
    def draw(self):
        self.camera_image = pygame.transform.scale(self.camera_image,(800,600))
        self.screen.blit(self.camera_image,(0,0))

    #draws the counselors
    def draw_counselor(self,file_path,pos,scale):
        image = pygame.image.load(file_path)
        image = pygame.transform.scale(image,scale)
        self.screen.blit(image,pos)
        
        


