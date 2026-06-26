import sys
import pygame
import os

class Camera:
    def __init__(self, screen: pygame.Surface, camera_image,image_folder,counselor_camera):
        self.screen = screen
        self.camera_image = pygame.image.load(camera_image)
        self.counselors_in_camera = counselor_camera
        self.counselors_images = []
        for image in os.listdir(image_folder):
            self.counselors_images.append(pygame.image.load(image))

    def draw(self):
        self.screen.blit(self.camera_image,(0,0))

    def is_counselor_there(self):
        for couns in self.counselors_in_camera:
            if couns == "carp":
                self.screen.blit()

