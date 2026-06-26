import sys
import pygame
import os
import counselor_module

class Camera:
    def __init__(self, screen: pygame.Surface, camera_image,image_folder):
        self.screen = screen
        self.camera_image = pygame.image.load(camera_image)
        self.counselors_in_camera = []
        self.counselors_images = []
        for image in os.listdir(image_folder):
            self.counselors_images.append(pygame.image.load(image))

    def draw(self):
        self.screen.blit(self.camera_image,(0,0))

    def is_counselor_there(self,name):
        self.screen.blit(name,(40,40))
        


