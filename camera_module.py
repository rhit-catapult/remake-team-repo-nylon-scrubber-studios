import sys
import pygame
import os
import counselor_module

class Camera:
    def __init__(self, screen: pygame.Surface, camera_image,image_folder):
        self.screen = screen
        self.camera_image = pygame.image.load(camera_image)
        self.counselors_in_camera = []
        self.folder = []
        for image in os.listdir(image_folder):
            self.folder.append(image)

    def load_images(self):
        self.ethan = pygame.image.load("cam1_images/")
        self.carp = pygame.image.load()
        self.aiman = pygame.image.load()
        self.jj = pygame.image.load()
        self.andrew = pygame.image.load()

    def draw(self):
        self.screen.blit(self.camera_image,(0,0))

    def draw_counselor(self,name,pos):
        if name == "ethan":
            self.screen.blit(self.ethan,pos)
        elif name == "aiman":
            self.screen.blit(self.aiman,pos)
        elif name == "carp":
            self.screen.blit(self.carp,pos)
        elif name == "jj":
            self.screen.blit(self.jj,pos)
        elif name == "andrew":
            self.screen.blit(self.andrew,pos)
        


