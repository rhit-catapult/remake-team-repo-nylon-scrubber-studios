import sys
import pygame
import camera_module
import counselor_module
import button_module
import time

from settings import *

class Camera_System:
    def __init__(self, screen: pygame.Surface, camera_on):

        self.screen = screen
        self.current_camera = 0
        self.count =0
        self.camera_on = camera_on
        self.minimap_image = pygame.image.load("images/minimap.png")
        self.minimap_image = pygame.transform.scale(self.minimap_image,(300,300))
        self.cameras = []
        self.last_click = 0
        self.delay = 200
        self.button = button_module.Buttons(screen,screen.get_width()/2-40,500,"images/button_test.png")
        self.camera_image_folders = ["images/cam1_images","images/cam2_images","images/cam3_images","images/cam4_images","images/cam5_images","images/cam6_images"]

    def load_everything(self):
        self.camera_1 = camera_module.Camera(self.screen, "images/cam1_main.jpg", 20,20)
        self.camera_2 = camera_module.Camera(self.screen, "images/cam2_main.jpg", 60,20)
        self.camera_3 = camera_module.Camera(self.screen, "images/cam3_main.jpg", 100,20)
        self.camera_4 = camera_module.Camera(self.screen, "images/cam4_main.jpg", 140,20)
        self.camera_5 = camera_module.Camera(self.screen, "images/cam5_main.jpg", 180,20)
        self.camera_6 = camera_module.Camera(self.screen, "images/cam6_main.jpg", 220,20)
        self.cameras.append(self.camera_1)
        self.cameras.append(self.camera_2)
        self.cameras.append(self.camera_3)
        self.cameras.append(self.camera_4)
        self.cameras.append(self.camera_5)
        self.cameras.append(self.camera_6)
        self.jj = counselor_module.Counselor(None,'jj',0,5,20)
        self.carp = counselor_module.Counselor(None,'carp',0,5,20)
        self.aiman = counselor_module.Aimen(50)
        self.ethan = counselor_module.Counselor(None,'ethan',0,5,20)
        self.andrew = counselor_module.Counselor(None,'andrew',0,5,20)


    def draw_minimap(self, minimap_x, minimap_y):
        self.screen.blit(self.minimap_image, (minimap_x, minimap_y))
        self.camera_1.button.draw(40,40)
        self.camera_2.button.draw(40,40)
        self.camera_3.button.draw(40,40)
        self.camera_4.button.draw(40,40)
        self.camera_5.button.draw(40,40)
        self.camera_6.button.draw(40,40)


    def constant_update(self):
        pass

    def update(self):
        self.draw()
        

        #Cam 1
        if self.camera_1.button.is_pressed_display() and pygame.time.get_ticks() - self.last_click > self.delay:
            self.last_click = pygame.time.get_ticks()
            self.switch_camera(0)

        #cam 2
        elif self.camera_2.button.is_pressed_display() and pygame.time.get_ticks() - self.last_click > self.delay:
            self.last_click = pygame.time.get_ticks()
            self.switch_camera(1)

        #cam 3
        elif self.camera_3.button.is_pressed_display() and pygame.time.get_ticks() - self.last_click > self.delay:
            self.last_click = pygame.time.get_ticks()
            self.switch_camera(2)

        elif self.camera_4.button.is_pressed_display() and pygame.time.get_ticks() - self.last_click > self.delay:
            self.last_click = pygame.time.get_ticks()
            self.switch_camera(3)

        elif self.camera_5.button.is_pressed_display() and pygame.time.get_ticks() - self.last_click > self.delay:
            self.last_click = pygame.time.get_ticks()
            self.switch_camera(4)

        elif self.camera_6.button.is_pressed_display() and pygame.time.get_ticks() - self.last_click > self.delay:
            self.last_click = pygame.time.get_ticks()
            self.switch_camera(5)

        if self.button.is_pressed_display() and pygame.time.get_ticks() - self.last_click > self.delay:
            self.last_click = pygame.time.get_ticks()
            self.camera_on = False
                    
            

    def switch_camera(self, camera_to_switch_to):
        self.current_camera = camera_to_switch_to

    def draw_cameras(self):
        #current_camera 0 corresponds to camera 1
        
        if self.current_camera == 0: #cam 1
            self.camera_1.draw()
            if self.jj.location == "kitchen(start)":
                self.camera_1.draw_counselor("images/jj/jj_pos1.png", (30,30),(800,600))
            if self.jj.location == "kitchen(middle)":
                self.camera_1.draw_counselor("images/jj/jj_pos2.png", (60,60),(800,600))
            if self.jj.location == "kitchen(end)":
                self.camera_1.draw_counselor("images/jj/jj_pos3.png", (90,90),(800,600))
            if self.ethan.location == "":
                self.camera_1.draw_counselor("images/eathen/ethan.jpg", (50,50),(800,600))
            if self.andrew.location == "":
                self.camera_1.draw_counselor("images/andrew/andrew_cam1.png", (70,70),(800,600))

        if self.current_camera == 1: #cam 2
            self.camera_2.draw()
            if self.carp.path[self.carp.location] == "livingroom":
                self.camera_2.draw_counselor("images/carp/carp_cam2.png", (0,0),(800,600))
            if self.ethan.location == "":
                self.camera_2.draw_counselor("images/eathen/ethan.jpg", (50,50),(800,600))

        elif self.current_camera == 2: #cam 3
            self.camera_3.draw()
            if self.ethan.location == "":
                self.camera_3.draw_counselor("images/eathen/ethan.jpg", (50,50),(800,600))
            if self.carp.path[self.carp.location] == "left_hallway":
                self.camera_3.draw_counselor("images/carp/carp_cam3_pos1.png", (0,0),(800,600))
            if self.carp.path[self.carp.location] == "peek":
                self.camera_3.draw_counselor("images/carp/carp_cam3_pos2.png", (0,0),(800,600))

        elif self.current_camera == 3: #cam 4
            self.camera_4.draw()
            if self.ethan.location == "":
                self.camera_4.draw_counselor("images/eathen/ethan.jpg", (50,50),(800,600))
            if self.andrew.location == "":
                self.camera_4.draw_counselor("images/andrew/andrew_cam4_pos1.png", (70,70),(800,600))

        elif self.current_camera == 4: #cam 5
            self.camera_5.draw()
            if self.carp.location == "left_doorway":
                self.camera_5.draw_counselor("images/eathen/ethan.jpg", (100,100),(800,600))
            if self.ethan.location == "":
                self.camera_5.draw_counselor("images/eathen/ethan.jpg", (40,40),(800,600))

        elif self.current_camera == 5: #cam 6
            self.camera_6.draw()
            self.camera_6.draw_counselor("images/aiman/aiman_cam6.png", (0,0),(800,600))

    def draw(self):
        self.draw_cameras()
        self.draw_minimap(400,400)
        self.button.draw(200,50)
        

def main():
    # turn on pygame
    pygame.init()
    pygame.display.set_caption("One Night at Catapult")
    screen = pygame.display.set_mode((800,600))

    #screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN | pygame.SCALED)
    camera_sys = Camera_System(screen,False)
    camera_sys.load_everything()
    aiman_button = button_module.Buttons(screen,50,450,"images/button_test.png")
    camera_button_office = button_module.Buttons(screen,screen.get_width()/2,500,"images/button_test.png")

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            mouse_pos = pygame.mouse.get_pos()
            if camera_sys.camera_on == False:
                if aiman_button.rect.collidepoint(mouse_pos):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print("clicked")
                if camera_button_office.rect.collidepoint(mouse_pos):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        camera_sys.camera_on = True
                        print("cam click")  
        
        screen.fill((255, 255, 255))

        #draws the office if cameras are off
        if camera_sys.camera_on == False:
            aiman_button.draw(40,40)
            camera_button_office.draw(100,50)
            camera_sys.last_click = pygame.time.get_ticks()

        #draws the cameras if cameras are on
        if camera_sys.camera_on:
            camera_sys.update()
            
        



        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

if __name__ == "__main__":
    main()