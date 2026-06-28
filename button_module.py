import pygame
import camera_system_module
import sys

class Buttons:
    def __init__(self, screen,x,y,image):
        self.screen = screen
        self.x = x
        self.y = y
        self.base_image = pygame.image.load(image).convert_alpha()
        self.image = self.base_image
        self.rect = pygame.Rect(x,y,self.image.get_width(),self.image.get_height())

    def draw(self, scale_x=None, scale_y=None):
        if scale_x is not None and scale_y is not None:
            self.image = pygame.transform.scale(self.base_image, (scale_x, scale_y))
        else:
            self.image = self.base_image

        self.rect.size = self.image.get_size()
        self.rect.topleft = (self.x, self.y)
        self.screen.blit(self.image, (self.x, self.y))

    def is_pressed_display(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()[0]
        return self.rect.collidepoint(mouse_pos) and mouse_press

    def is_pressed(self, pos):
        return self.rect.collidepoint(pos)
    



def main():
    pygame.init()
    pygame.display.set_caption("One Night at Catapult")
    screen = pygame.display.set_mode((800,600))
    aiman_button = Buttons(screen,50,400,"images/button_test.png")

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if aiman_button.rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("clicked")

        screen.fill((255, 255, 255))
        aiman_button.draw()

        pygame.display.update()
    
if __name__ == "__main__":
    main()