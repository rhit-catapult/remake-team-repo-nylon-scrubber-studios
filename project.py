import pygame
import sys
import random
import time
import os
import camera_system_module
import button_module
import office_module

from settings import *

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
    camera_button_office = button_module.Buttons(screen,screen.get_width()/2,500,"images/button_test.png")
    count = 0

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

        #office side scrolling
        if left_rect.collidepoint(pygame.mouse.get_pos()):
            office.move("left")
        elif right_rect.collidepoint(pygame.mouse.get_pos()):
            office.move("right")     
        
        screen.fill((255, 255, 255))

        #draws the office if cameras are off
        if camera_sys.camera_on == False:
            office.draw()
            aiman_button.draw(40,40)
            camera_button_office.draw(100,50)
            camera_sys.last_click = pygame.time.get_ticks()

        #draws the cameras if cameras are on
        if camera_sys.camera_on:
            camera_sys.update()
            
        



        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

main()


