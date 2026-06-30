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
        self.minimap_image = pygame.image.load("images/mini_map.png")
        self.minimap_image = pygame.transform.scale(self.minimap_image,(300,300))
        self.last_click = 0
        self.delay = 200
        self.button = button_module.Buttons(screen,200,550,"images/camera_button_down.png.png")

    def load_everything(self):
        last_start_time = pygame.time.get_ticks()
        
        #Setting up Camera's
        self.camera_1 = camera_module.Camera(self.screen, "images/cam1_main.jpg", 735,542,1)
        self.camera_2 = camera_module.Camera(self.screen, "images/cam2_main.jpg", 647,483,2)
        self.camera_3 = camera_module.Camera(self.screen, "images/cam3_main.jpg", 670,358,3)
        self.camera_4 = camera_module.Camera(self.screen, "images/cam4_main.jpg", 740,358,4)
        self.camera_5 = camera_module.Camera(self.screen, "images/cam5_main.jpg", 668,308,5)
        self.camera_6 = camera_module.Camera(self.screen, "images/cam6_main.jpg", 740,323,6)

        #Setting up Counselors
        self.jj = counselor_module.Counselor(None,'jj',0,5,5,last_start_time)
        self.carp = counselor_module.Counselor(None,'carp',0,5,5,last_start_time)
        self.aiman = counselor_module.Aimen(50)
        self.ethan = counselor_module.Counselor(None,'ethan',0,5,5,last_start_time)
        self.andrew = counselor_module.Counselor(None,'andrew',0,5,5,last_start_time)

        #Initializing the paths of counselors
        self.jj.get_counselor()
        self.carp.get_counselor()
        self.ethan.get_counselor()
        self.andrew.get_counselor()

        #Resets their positions
        self.jj.reset()
        self.carp.reset()
        self.ethan.reset()
        self.andrew.reset()
        self.aiman.aimen_button_pushed()



    def draw_minimap(self, minimap_x, minimap_y):
        self.screen.blit(self.minimap_image, (minimap_x, minimap_y))
        self.camera_1.button.draw(25,20)
        self.camera_2.button.draw(25,20)
        self.camera_3.button.draw(25,20)
        self.camera_4.button.draw(25,20)
        self.camera_5.button.draw(25,20)
        self.camera_6.button.draw(25,20)

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
            camera_up = pygame.mixer.Sound('sounds/camera_down.wav')
            pygame.mixer.music.set_volume(2.0)
            camera_up.play()
            self.last_click = pygame.time.get_ticks()
            self.camera_on = False
                    
            

    def switch_camera(self, camera_to_switch_to):
        pygame.mixer.Sound('sounds/camera_switch.wav').play()
        self.current_camera = camera_to_switch_to

    def draw_cameras(self):
        #current_camera 0 corresponds to camera 1
        if self.current_camera == 0: #cam 1
            self.camera_1.draw()
            if self.jj.path[self.jj.location] == "kitchen(start)":
                self.camera_1.draw_counselor("images/jj/jj_pos1.png", (0,-1.9),(800,600))
            if self.jj.path[self.jj.location] == "kitchen(middle)":
                self.camera_1.draw_counselor("images/jj/jj_pos2.png", (14,-35),(800,600))
            if self.jj.get_counselor() == "kitchen(end)":
                self.camera_1.draw_counselor("images/jj/jj_pos3.png", (15,-29),(800,600))
            if self.ethan.path[self.ethan.location] == "kitchen":
                self.camera_1.draw_counselor("images/eathen/ethan.png", (0,0),(80,60))
            if self.andrew.path[self.andrew.location] == "kitchen":
                self.camera_1.draw_counselor("images/andrew/andrew_cam1.png", (-60,-10),(800,600))

        if self.current_camera == 1: #cam 2
            self.camera_2.draw()
            if self.carp.get_counselor() == "livingroom":
                self.camera_2.draw_counselor("images/carp/carp_cam2.png", (-100,70),(800,600))
            if self.ethan.path[self.ethan.location] == "livingroom":
                self.camera_2.draw_counselor("images/eathen/ethan.png", (0,0),(800,600))

        elif self.current_camera == 2: #cam 3
            self.camera_3.draw()
            if self.ethan.path[self.ethan.location] == "left_hall":
                self.camera_3.draw_counselor("images/eathen/ethan.png", (0,0),(800,600))
            if self.carp.path[self.carp.location] == "left_hallway":
                self.camera_3.draw_counselor("images/carp/carp_cam3_pos1.png", (-5,140),(800,600))
            if self.carp.path[self.carp.location] == "peek":
                self.camera_3.draw_counselor("images/carp/carp_cam3_pos2.png", (5,150),(800,600))

        elif self.current_camera == 3: #cam 4
            self.camera_4.draw()
            if self.ethan.path[self.ethan.location] == "right_hall":
                self.camera_4.draw_counselor("images/eathen/ethan.png", (0,0),(800,600))
            if self.andrew.path[self.andrew.location] == "right_hall_far":
                self.camera_4.draw_counselor("images/andrew/andrew_cam4_pos1.png", (0,15),(800,600))
            if self.andrew.path[self.andrew.location] == "right_hall_close":
                self.camera_4.draw_counselor("images/andrew/andrew_cam4_pos2.png",(-10,30),(800,600))
            

        elif self.current_camera == 4: #cam 5
            self.camera_5.draw()
            if self.ethan.path[self.ethan.location] == "restroom":
                self.camera_5.draw_counselor("images/eathen/ethan.png", (0,0),(800,600))

        elif self.current_camera == 5: #cam 6
            self.camera_6.draw()
            self.camera_6.draw_counselor("images/aiman/aiman_cam6.png", (-30,100),(800,600))
            self.screen.blit(self.aiman.aiman_timer_text,(20,0))

    def draw(self):
        self.draw_cameras()
        self.draw_minimap(530,300)
        self.button.draw(400,50)
        

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