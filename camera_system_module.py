import sys
import pygame
import camera_module
import counselor_module

class Camera_System:
    def __init__(self, screen: pygame.Surface, camera_on):
        self.screen = screen
        self.current_camera = 0
        self.camera_on = camera_on
        self.minimap_image = pygame.image.load("images/test_picture.png")
        self.cameras = []
        self.camera_image_folders = ["images/cam1_images","images/cam2_images","images/cam3_images","images/cam4_images","images/cam5_images","images/cam6_images"]

    def load_everything(self):
        self.camera_1 = camera_module.Camera(self.screen, "images/cam2_main.jpg", self.camera_image_folders[0])
        self.camera_2 = camera_module.Camera(self.screen, "images/cam2_main.jpg", self.camera_image_folders[1])
        self.camera_3 = camera_module.Camera(self.screen, "images/cam2_main.jpg", self.camera_image_folders[2])
        self.camera_4 = camera_module.Camera(self.screen, "images/cam2_main.jpg", self.camera_image_folders[3])
        self.camera_5 = camera_module.Camera(self.screen, "images/cam2_main.jpg", self.camera_image_folders[4])
        self.camera_6 = camera_module.Camera(self.screen, "images/cam2_main.jpg", self.camera_image_folders[5])
        self.cameras.append(self.camera_1)
        self.cameras.append(self.camera_2)
        self.cameras.append(self.camera_3)
        self.cameras.append(self.camera_4)
        self.cameras.append(self.camera_5)
        self.cameras.append(self.camera_6)
        for i in self.cameras:
            i.load_images()
        self.jj = counselor_module.Counselor(None,'jj',2,5,20)
        self.carp = counselor_module.Counselor(None,'carp',2,5,20)
        self.aiman = counselor_module.Counselor(None,'aiman',2,5,20)
        self.ethan = counselor_module.Counselor(None,'ethan',2,5,20)
        self.andrew = counselor_module.Counselor(None,'andrew',2,5,20)


    def draw_minimap(self, minimap_x, minimap_y):
        self.screen.blit(self.minimap_image, (minimap_x, minimap_y))

    def camera_on_or_off(self):
        if self.camera_on:
            self.draw_cameras()
            self.draw_minimap(400,400)

    def switch_camera(self, camera_to_switch_to):
        self.current_camera = camera_to_switch_to

    def draw_cameras(self):
        #current_camera 0 corresponds to camera 1
        
        if self.current_camera == 0: #cam 1
            self.camera_1.draw()
            if self.jj.location == "kitchen(start)":
                self.camera_1.draw_counselor("jj", (30,30))
            if self.jj.location == "kitchen(middle)":
                self.camera_1.draw_counselor("jj", (60,60))
            if self.jj.location == "kitchen(end)":
                self.camera_1.draw_counselor("jj", (90,90))
            if self.ethan.location == "":
                self.camera_1.draw_counselor("ethan", (50,50))
            if self.andrew.location == "":
                self.camera_1.draw_counselor("andrew", (70,70))

        elif self.current_camera == 1: #cam 2
            self.camera_2.draw()
            if self.carp.location == "livingroom":
                self.camera_2.draw_counselor("carp", (50,50))
            if self.ethan.location == "":
                self.camera_2.draw_counselor("ethan", (50,50))

        elif self.current_camera == 2: #cam 3
            self.camera_3.draw()
            if self.ethan.location == "":
                self.camera_3.draw_counselor("ethan", (50,50))
            if self.carp.location == "left_hallway":
                self.camera_3.draw_counselor("carp", (50,50))
            if self.carp.location == "peek":
                self.camera_3.draw_counselor("carp", (100,100))

        elif self.current_camera == 3: #cam 4
            self.camera_4.draw()
            if self.ethan.location == "":
                self.camera_4.draw_counselor("ethan", (50,50))
            if self.andrew.location == "":
                self.camera_4.draw_counselor("andrew", (70,70))

        elif self.current_camera == 4: #cam 5
            self.camera_5.draw()
            if self.carp.location == "left_doorway":
                self.camera_5.draw_counselor("carp", (100,100))
            if self.ethan.location == "":
                self.camera_5.draw_counselor("ethan", (40,40))

        else: #cam 6
            self.camera_6.draw()
            if self.aiman.location == "":
                self.camera_6.draw_counselor("aiman", (100,100))
    def draw(self):
        #self.draw_cameras()
        self.draw_minimap(400,400)
        