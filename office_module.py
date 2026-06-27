import pygame
import sys
import button_module

class Office:
    def __init__(self,screen: pygame.Surface,image,camera_off):
        self.screen = screen
        self.image = pygame.image.load(image)
        self.x = -200
        self.cam_off = camera_off

    def draw(self):
        if self.cam_off:
            self.image = pygame.transform.scale(self.image,(1200,600))
            self.screen.blit(self.image,(self.x,0))

    def move(self,direction):
        if direction == "left" and self.x < 0:
            self.x += 2
        elif direction == "right" and self.x > -200:
            self.x -= 2



#test function
def main():
    # turn on pygame
    pygame.init()
    pygame.display.set_caption("One Night at Catapult")
    screen = pygame.display.set_mode((800,600))
    office = Office(screen,"images/office.jpg",False)

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        screen.fill((255, 255, 255))

        office.draw()



        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

if __name__ == "__main__":
    main()