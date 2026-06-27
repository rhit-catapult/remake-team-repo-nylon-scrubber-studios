import pygame
import sys
import random
import time
import os
import camera_system_module
import button_module
import office_module

def main():
    # turn on pygame
    pygame.init()
    pygame.display.set_caption("One Night at Catapult")
    screen = pygame.display.set_mode((800,600))
    #screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN | pygame.SCALED)
    camera_sys = camera_system_module.Camera_System(screen,False)
    camera_sys.load_everything()
    office = office_module.Office(screen,"images/office.jpg",True)
    left_rect = pygame.Rect(0,0,40,600)
    right_rect = pygame.Rect(760,0,40,600)
    aiman_button = button_module.Buttons(screen,50,450,"images/button_test.png")
    camera_button = button_module.Buttons(screen,screen.get_width()/2,500,"images/button_test.png")

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if aiman_button.rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("clicked")
            if camera_button.rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN and camera_sys.camera_on == False:
                    camera_sys.camera_on = True
                

        #office side scrolling
        if left_rect.collidepoint(pygame.mouse.get_pos()):
            office.move("left")
        elif right_rect.collidepoint(pygame.mouse.get_pos()):
            office.move("right")

        
        

        screen.fill((255, 255, 255))

        office.draw()
        aiman_button.draw()
        camera_button.draw()
        camera_sys.camera_on_or_off()



        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

main()


