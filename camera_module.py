import sys
import pygame
import os
import counselor_module

class Camera:

    #creates a camera
    def __init__(self, screen: pygame.Surface, camera_image,image_folder):
        self.screen = screen
        self.camera_image = pygame.image.load(camera_image)
        self.counselors_in_camera = []
        self.folder = []
        camera_num = 0
        for image in os.listdir(image_folder):
            camera_num+=1
            self.folder.append(f"images/cam{camera_num}_images/{image}")

    #loads the image files into a variable
    def load_images(self):
        self.ethan = pygame.image.load(self.folder[2])
        self.carp = pygame.image.load(self.folder[1])
        self.jj = pygame.image.load(self.folder[3])
        self.andrew = pygame.image.load(self.folder[0])

    #draws the camera
    def draw(self):
        self.screen.blit(self.camera_image,(0,0))

    #draws the counselors
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
        


