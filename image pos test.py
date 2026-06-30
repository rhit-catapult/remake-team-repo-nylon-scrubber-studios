import pygame
import sys

import camera_module

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image Test")

camera_object = camera_module.Camera(screen, "images/cam1_main.jpg", 100,20)
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





# DON'T DELETE THE FOLLOWING:
# draw_counselor("images/jj/jj_pos1.png", (0,-1.9),(800,600))
# draw_counselor("images/jj/jj_pos2.png", (14,-35),(800,600))
# draw_counselor("images/jj/jj_pos3.png", (15,-29),(800,600))
# draw_counselor("images/andrew/andrew_cam1.png", (-60,-10),(800,600))

# draw_counselor("images/carp/carp_cam2.png", (-100,70),(800,600))

# draw_counselor("images/carp/carp_cam3_pos1.png", (-5,140),(800,600))
# draw_counselor("images/carp/carp_cam3_pos2.png", (5,150),(800,600))

# draw_counselor("images/andrew/andrew_cam4_pos1.png",(0,15),(800,600))
# draw_counselor("images/andrew/andrew_cam4_pos2.png",(-10,30),(800,600))

# draw_counselor("images/aiman/aiman_cam6.png", (-30,100),(800,600))


# camera_module.Camera(self.screen, "images/cam1_main.jpg", 730,535)
# camera_module.Camera(self.screen, "images/cam2_main.jpg", 640,470)
# camera_module.Camera(self.screen, "images/cam3_main.jpg", 662,350)
# camera_module.Camera(self.screen, "images/cam4_main.jpg", 733,350)
# camera_module.Camera(self.screen, "images/cam5_main.jpg", 662,300)
# camera_module.Camera(self.screen, "images/cam6_main.jpg", 733,310)