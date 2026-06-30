import pygame
import sys

import camera_module

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image Test")

camera_object = camera_module.Camera(screen, "images/cam6_main.jpg", 100,20)
image_test = pygame.image.load("images/cam6_main.jpg")
image_test = pygame.transform.scale(image_test, (800, 600))


while True:
    screen.fill((0, 0, 0))
    screen.blit(image_test, (0, 0))
    camera_object.draw_counselor("images/aiman/aiman_cam6.png", (-30,100),(800,600))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()