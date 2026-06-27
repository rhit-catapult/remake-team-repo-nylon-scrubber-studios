import pygame
import camera_system_module
import sys

class Buttons:
    def __init__(self, screen,x,y,image):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.rect = pygame.Rect(x,y,self.image.get_width(),self.image.get_height())

    
    def draw(self):
        self.screen.blit(self.image,(self.x,self.y))

    #determine if button was pushed
    def is_pressed(self,pos):
        posx = pos[0]
        posy = pos[1]
        return (self.x < posx < self.image.get_width() and self.y < posy < self.image.get_height)
    
def main():
    pygame.init()
    pygame.display.set_caption("One Night at Catapult")
    screen = pygame.display.set_mode((800,600))
    aiman_button = Buttons(screen,50,400,"images/button_test.png")

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

        

        

        screen.fill((255, 255, 255))
        aiman_button.draw()



        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()
    
if __name__ == "__main__":
    main()