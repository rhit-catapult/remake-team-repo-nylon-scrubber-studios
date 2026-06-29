import pygame
import sys
import button_module

class Office:
    def __init__(self,screen: pygame.Surface,image,camera_off,is_here,door_side: str):
        self.screen = screen
        self.image = pygame.image.load(image)
        self.x = -200
        self.cam_off = camera_off
        self.door_closed = False
        self.here = is_here
        self.door = Door(f"images/office_{door_side}_closed.jpg",screen)
        self.door_button = button_module.Buttons(screen,20,400,"images/button_test.png")

    def draw(self):
        if self.cam_off:
            self.image = pygame.transform.scale(self.image,(1200,600))
            self.screen.blit(self.image,(self.x,0))
            self.door.draw()
            self.door_button.draw(40,40)


    


class Door:
    def __init__(self,filename: str,screen: pygame.Surface,):
        self.closed = False
        self.screen = screen
        self.image = pygame.image.load(filename)
    
    def draw(self):
        self.screen.blit(self.image,(40,80))

    def is_closed(self):
        return self.closed

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