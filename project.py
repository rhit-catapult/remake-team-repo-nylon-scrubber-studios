import pygame
import sys
import random
import timer_module
import camera_system_module
import button_module
import office_module
import start_end_screen_module

from settings import *

def main():
    # turn on pygame
    pygame.init()
    pygame.display.set_caption("One Night at Catapult")
    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    #screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN | pygame.SCALED)
    run = False
    game_over = False
    win = False

    #Timer
    timer = timer_module.Timer(screen,100,200,"images/clock.png",100,50,72000)

    #Camera System
    camera_sys = camera_system_module.Camera_System(screen,False)

    #The Office
    office_main = office_module.Office(screen,"images/office_main.jpg",True,True,None)
    office_left = office_module.Office(screen,"images/office_left.png",True,False,"left",(30,300))
    office_right = office_module.Office(screen,"images/office_right.png",True,False,"right",(500,300))
    left_rect = pygame.Rect(0,0,40,WINDOW_HEIGHT)
    right_rect = pygame.Rect(760,0,40,WINDOW_HEIGHT)
    left_true = False
    right_true = False

    #Buttons
    aiman_button = button_module.Buttons(screen,50,450,"images/button_test.png")
    camera_button_office = button_module.Buttons(screen,WINDOW_WIDTH/2,500,"images/button_test.png")
    carp_button = button_module.Buttons(screen,300,450, "images/button_test.png")
    
    #Jumpscares
    carp_jumpscare = pygame.image.load("images/carp/carp_jumpscare.png")
    carp_jumpscare = pygame.transform.scale(carp_jumpscare,(WINDOW_WIDTH,WINDOW_HEIGHT))
    jj_jumpscare = pygame.image.load("images/jj/jj_jumpscare.png")
    jj_jumpscare = pygame.transform.scale(jj_jumpscare,(WINDOW_WIDTH,WINDOW_HEIGHT))
    aiman_jumpscare = pygame.image.load("images/aiman/aiman_jumpscare.png")
    aiman_jumpscare = pygame.transform.scale(aiman_jumpscare,(WINDOW_WIDTH,WINDOW_HEIGHT))
    andrew_jumpscare = pygame.image.load("images/andrew/andrew_jumpscare.png")
    andrew_jumpscare = pygame.transform.scale(andrew_jumpscare,(WINDOW_WIDTH,WINDOW_HEIGHT))

    #Other screens
    other_screen = start_end_screen_module.Start_Screen(screen)

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        dt = clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            mouse_pos = pygame.mouse.get_pos()
            if other_screen.game_over_button.is_pressed_display() and game_over == True:
                game_over = False
                run = False
            if other_screen.start_button.is_pressed_display() and run == False:
                run = True
                camera_sys.load_everything()
            if other_screen.win_button.is_pressed_display() and win == True:
                win = False
                timer.win_condition = False
                timer.reset_clock(720000)

                
            if run:
                if camera_sys.camera_on == False:
                    if aiman_button.rect.collidepoint(mouse_pos):
                        if event.type == pygame.MOUSEBUTTONDOWN and camera_sys.aiman.aimen_awake == False:
                            camera_sys.aiman.aimen_button_pushed()
                    if camera_button_office.rect.collidepoint(mouse_pos):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            camera_up = pygame.mixer.Sound('sounds/camera_up.wav')
                            pygame.mixer.music.set_volume(2.0)
                            camera_up.play()
                            camera_sys.camera_on = True
                    if carp_button.rect.collidepoint(mouse_pos):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            camera_sys.carp.carp_button_pushed()

        if run:            
            #Background
            screen.fill((255, 255, 255))

            #checks and stops counselors from jumpscaring if the door is closed
            if office_left.door_closed == True:
                camera_sys.jj.door = True
            else:
                camera_sys.jj.door = False
            if office_right.door_closed == True:
                camera_sys.andrew.door = True
            else:
                camera_sys.andrew.door = False

            #draws the office if cameras are off
            if camera_sys.camera_on == False:
                #office side scrolling
                left_rect_collision = left_rect.collidepoint(pygame.mouse.get_pos())
                right_rect_collision = right_rect.collidepoint(pygame.mouse.get_pos())

                if not left_rect_collision:
                    left_true = False
                if not right_rect_collision:
                    right_true = False

                if left_rect_collision and office_main.here and not left_true:
                    office_main.here = False
                    office_left.here = True
                    left_true = True
                elif left_rect_collision and office_right.here and not left_true:
                    office_right.here = False
                    office_main.here = True
                    left_true = True
                if right_rect_collision and office_left.here and not right_true:
                    office_left.here = False
                    office_main.here = True
                    right_true = True
                elif right_rect_collision and office_main.here and not right_true:
                    office_main.here = False
                    office_right.here = True
                    right_true = True

                #updates office sides
                office_left.update()
                office_right.update()
                if office_main.here:
                    office_main.draw()
                    aiman_button.draw(40,40)
                    carp_button.draw(40,40)
                    timer.draw()
                    camera_button_office.draw(100,50)
                elif office_left.here:
                    office_left.draw("left")
                elif office_right.here:
                    office_right.draw("left")
                camera_sys.last_click = pygame.time.get_ticks()

            #draws the cameras if cameras are on
            if camera_sys.camera_on:
                camera_sys.update()

            timer.time_length -= dt
            if timer.win_condition:
                win = True
                run = False

            #carp jumpscare
            if camera_sys.carp.kill:
                pygame.draw.rect(screen,"black",(0,0,WINDOW_WIDTH,WINDOW_HEIGHT))
                screen.blit(carp_jumpscare,(0,0))
                if pygame.time.get_ticks() >= camera_sys.carp.jump_time_start:
                    game_over = True
                    run = False
                    camera_sys.carp.kill = False

            #jj jumpscare
            if camera_sys.jj.kill:
                pygame.draw.rect(screen,"black",(0,0,WINDOW_WIDTH,WINDOW_HEIGHT))
                screen.blit(jj_jumpscare,(0,0))
                if pygame.time.get_ticks() >= camera_sys.jj.jump_time_start:
                    game_over = True
                    run = False
                    camera_sys.jj.kill = False

            #andrew jumpscare
            if camera_sys.andrew.kill:
                pygame.draw.rect(screen,"black",(0,0,WINDOW_WIDTH,WINDOW_HEIGHT))
                screen.blit(andrew_jumpscare,(0,0))
                if pygame.time.get_ticks() >= camera_sys.andrew.jump_time_start:
                    game_over = True
                    run = False
                    camera_sys.andrew.kill = False

            #Aiman jumpscare
            if camera_sys.aiman.aimen_awake:
                pygame.draw.rect(screen,"black",(0,0,WINDOW_WIDTH,WINDOW_HEIGHT))
                screen.blit(aiman_jumpscare,(0,0))
                if pygame.time.get_ticks() >= camera_sys.aiman.jump_time_start:
                    game_over = True
                    run = False

            
            camera_sys.aiman.aimen_clock()
            ethan = camera_sys.ethan
            camera_sys.carp.movement(ethan)
            camera_sys.andrew.movement(ethan)
            camera_sys.jj.movement(ethan)
        elif game_over:
            other_screen.draw_game_over_screen(100)
        elif win:
            other_screen.draw_win_screen(100)
        else: 
            other_screen.draw_start_screen(100)

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

main()


