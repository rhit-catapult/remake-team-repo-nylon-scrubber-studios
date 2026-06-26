import sys
import pygame
import camera
import counselor_module

class Camera_System:
    def __init__(self, screen, camera_on):
        self.screen = screen
        self.current_camera = 0
        self.camera_on = camera_on
        #self.minimap_image = pygame.image.load("")
        self.cameras = []
        self.camera_image_folders = ["","","","","",""]
        for i in range(6):
            self.cameras.append(camera.Camera())

    def Draw_Minimap(self, minimap_x, minimap_y):
        self.screen.blit(self.minimap_image, (minimap_x, minimap_y))
    def Camera_On_or_Off(self):
        if self.camera_on:
            self.Draw_Minimap
    def Are_Counselors_There(self):
        counselor_module.counselor_locations
    def Switch_Camera(self, camera_to_switch_to):
        camera.Camera.draw(camera_to_switch_to)