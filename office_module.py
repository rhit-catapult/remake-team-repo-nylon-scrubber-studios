import pygame
import sys
import button_module


from settings import *

class Office:
    def __init__(self,screen: pygame.Surface,image,camera_off,is_here,door_side = None,door_button_position = (-100,-100)):
        self.screen = screen
        self.image = pygame.image.load(image)
        self.x = -200
        self.cam_off = camera_off
        self.door_closed = False
        self.here = is_here
        if door_side != None:
            self.door = Door(f"images/office_{door_side}_closed.jpg",screen)
            self.door_button = button_module.Buttons(screen,door_button_position[0],door_button_position[1],"images/button_test.png")
        else:
            self.door = None
        

    def draw(self):
        if self.cam_off:
            self.image = pygame.transform.scale(self.image,(1200,600))
            self.screen.blit(self.image,(self.x,0))
            if self.door != None:
                self.door_button.draw(40,40)
                if self.door_closed:
                    self.door.draw()
            

    def update(self):
        if self.door_button.is_pressed_display():
            self.door_closed = True
        else:
            self.door_closed = False


class Door:
    def __init__(self,filename: str,screen: pygame.Surface,):
        self.closed = False
        self.screen = screen
        self.image = pygame.image.load(filename)
    
    def draw(self):
        self.image = pygame.transform.scale(self.image,(WINDOW_WIDTH,WINDOW_HEIGHT))
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