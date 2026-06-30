import pygame
import sys
import button_module



from settings import *

class Office:
    def __init__(self,screen: pygame.Surface,image,camera_off,is_here,door_side = None,door_button_position = (-100,-100)):
        self.screen = screen
        self.image = pygame.image.load(image)
        self.x = 0
        self.cam_off = camera_off
        self.door_closed = False
        self.here = is_here
        self.current_color = (0,0,0)
        self.is_counselor_here = False
        self.button_pos = door_button_position
        if door_side != None:
            if door_side == "left":
                self.rect = pygame.Rect(278,0,182,520)
            elif door_side == "right":
                self.rect = pygame.Rect(320,0,210,520)
                pygame.draw.rect(screen,(0,0,0),(320,0,210,520))
            self.door = Door(f"images/office_{door_side}door_closed.png",screen,door_side)
            self.door_button = button_module.Buttons(screen,door_button_position[0],door_button_position[1],"images/door_button_off.png")
            self.button_color = (255,0,0)
        else:
            self.door = None
        

    def draw(self,side = None):
        if self.cam_off:
            self.image = pygame.transform.scale(self.image,(800,600))
            if side == "left":
                pygame.draw.rect(self.screen,self.current_color,(240,0,250,530))
            elif side == "right":
                pygame.draw.rect(self.screen,self.current_color,(300,0,240,520))
            self.screen.blit(self.image,(self.x,0))
            if self.door != None:
                pygame.draw.rect(self.screen,self.button_color,(self.button_pos[0],self.button_pos[1],40,40))
                self.door_button.draw(40,40)
                if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.current_color = (160,160,160)
                    self.is_counselor_here = True
                else:
                    self.current_color = (0,0,0)
                    self.is_counselor_here = False
                if self.door_closed:
                    self.door.draw()
                
            

    def update(self):
        if self.door_button.is_pressed_display():
            self.door_closed = True
            self.button_color = (0,255,0)
        else:
            self.door_closed = False
            self.button_color = (255,0,0)
            
            


class Door:
    def __init__(self,filename: str,screen: pygame.Surface,door_side):
        self.closed = False
        self.screen = screen
        self.image = pygame.image.load(filename)
    
    def draw(self):
        self.image = pygame.transform.scale(self.image,(WINDOW_WIDTH,WINDOW_HEIGHT))
        self.screen.blit(self.image,(0,0))


#test function
def main():
    # turn on pygame
    pygame.init()
    pygame.display.set_caption("One Night at Catapult")
    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    #screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN | pygame.SCALED)

    #The Office
    office_main = Office(screen,"images/office_main.jpg",True,True,None)
    office_left = Office(screen,"images/office_left.png",True,False,"left",(30,300))
    office_right = Office(screen,"images/office_right.png",True,False,"right",(500,300))
    left_rect = pygame.Rect(0,0,40,WINDOW_HEIGHT)
    right_rect = pygame.Rect(760,0,40,WINDOW_HEIGHT)
    left_true = False
    right_true = False

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        dt = clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)

        if True:            
            #Background
            screen.fill((255, 255, 255))

            #draws the office if cameras are off
            if True:
                #office side scrolling
                left_rect_collision = left_rect.collidepoint(pygame.mouse.get_pos())
                right_rect_collision = right_rect.collidepoint(pygame.mouse.get_pos())

                if not left_rect_collision:
                    pygame.mixer.Sound('sounds/door_open.wav').play()
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
                elif office_left.here:
                    office_left.draw("left")
                elif office_right.here:
                    office_right.draw("right")

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

if __name__ == "__main__":
    main()