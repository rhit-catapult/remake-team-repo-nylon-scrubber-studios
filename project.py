import pygame
import sys
import random
import time
import os

def main():
    # turn on pygame
    pygame.init()
    pygame.display.set_caption("One Night at Catapult")
    screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN | pygame.SCALED)

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        screen.fill((255, 255, 255))



        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

main()


