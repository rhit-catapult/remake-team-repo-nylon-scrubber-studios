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

    def Make_Cameras(self):
        self.camera_1 = camera.Camera(self.screen, "*image*", "*image folder*", )
        self.camera_2 = camera.Camera()
        self.camera_3 = camera.Camera()
        self.camera_4 = camera.Camera()
        self.camera_5 = camera.Camera()
        self.camera_6 = camera.Camera()

    def Draw_Minimap(self, minimap_x, minimap_y):
        self.screen.blit(self.minimap_image, (minimap_x, minimap_y))
    def Camera_On_or_Off(self):
        if self.camera_on:
            self.Draw_Minimap
    def Switch_Camera(self, camera_to_switch_to):
        self.current_camera = camera_to_switch_to
        camera.Camera.draw((camera_to_switch_to))