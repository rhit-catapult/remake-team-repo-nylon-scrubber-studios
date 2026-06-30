import pygame
import sys

import camera_module

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image Test")

camera_object = camera_module.Camera(screen, "images/cam1_main.jpg", 20, 20)
image_test = pygame.image.load("images/cam1_main.jpg")
image_test = pygame.transform.scale(image_test, (800, 600))


while True:
    screen.fill((0, 0, 0))
    screen.blit(image_test, (0, 0))
    camera_object.draw_counselor("images/andrew/andrew_cam1.png", (-60,-10),(800,600))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()