import sys
import pygame
import camera_module
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
        self.camera_1 = camera_module.Camera(self.screen, "*image*", "*image folder*")
        self.camera_2 = camera_module.Camera(self.screen, "*image*", "*image folder*")
        self.camera_3 = camera_module.Camera(self.screen, "*image*", "*image folder*")
        self.camera_4 = camera_module.Camera(self.screen, "*image*", "*image folder*")
        self.camera_5 = camera_module.Camera(self.screen, "*image*", "*image folder*")
        self.camera_6 = camera_module.Camera(self.screen, "*image*", "*image folder*")
        self.cameras.append(self.camera_1)
        self.cameras.append(self.camera_2)
        self.cameras.append(self.camera_3)
        self.cameras.append(self.camera_4)
        self.cameras.append(self.camera_5)
        self.cameras.append(self.camera_6)

    def Draw_Minimap(self, minimap_x, minimap_y):
        self.screen.blit(self.minimap_image, (minimap_x, minimap_y))
    def Camera_On_or_Off(self):
        if self.camera_on:
            self.Draw_Minimap(400,400)
    def Looking_at_Which_Camera(self, camera_to_switch_to):
        self.cameras[camera_to_switch_to].draw()
        camera_module.camera_module.draw((camera_to_switch_to))
    def Counselors_in_Camera(self,current_camera):
        #current_camera 0 corresponds to camera 1
        if current_camera == 0:

        elif current_camera == 1:
            
        elif current_camera == 2:
        
        elif current_camera == 3:
        
        elif current_camera == 4:
        
        else:
            