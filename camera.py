import sys
import pygame

class Camera:
    def __init__(self, screen, current_camera, camera_image):
        self.screen = screen
        
        self.camera_image = pygame.image.load(camera_image)
        self.counselors_in_camera = []
        self.counselors_images = []

    def draw(self):

        pass
    def is_Counselor_There(self):
        pass
