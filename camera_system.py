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

    def load_everything(self):
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
        for i in self.cameras:
            i.load_images()


    def draw_minimap(self, minimap_x, minimap_y):
        self.screen.blit(self.minimap_image, (minimap_x, minimap_y))

    def camera_on_or_off(self):
        if self.camera_on:
            self.draw_minimap(400,400)

    def switch_camera(self, camera_to_switch_to):
        self.current_camera = self.cameras[camera_to_switch_to]
        camera_module.camera_module.draw((camera_to_switch_to))

    def draw_counselors_in_camera(self,current_camera):
        #current_camera 0 corresponds to camera 1
        if current_camera == 0:
            if counselor_module.carp.location == "":
                self.camera_1.draw_counselor("jj", (30,30))
            if counselor_module.ethan.location == "":
                self.camera_1.draw_counselor("ethan", (50,50))
            if counselor_module.andrew.location == "":
                self.camera_1.draw_counselor("andrew", (70,70))
        elif current_camera == 1:
            if counselor_module.carp.location == "":
                self.camera_2.draw_counselor("carp", (50,50))
            if counselor_module.ethan.location == "":
                self.camera_2.draw_counselor("ethan", (50,50))
        elif current_camera == 2:
            if counselor_module.ethan.location == "":
                self.camera_3.draw_counselor("ethan", (50,50))
            if counselor_module.carp.location == "":
                self.camera_3.draw_counselor("carp", (50,50))
        elif current_camera == 3:
            if counselor_module.ethan.location == "":
                self.camera_4.draw_counselor("ethan", (50,50))
            if counselor_module.andrew.location == "":
                self.camera_4.draw_counselor("andrew", (70,70))
        elif current_camera == 4:
            if counselor_module.carp.location == "":
                self.camera_5.draw_counselor("carp", (100,100))
            if counselor_module.ethan.location == "":
                self.camera_5.draw_counselor("ethan", (40,40))

        else:
            if counselor_module.aiman.location == "":
                self.camera_6.draw_counselor("aiman", (100,100))
    def draw(self):
        self.draw_counselors_in_camera()
