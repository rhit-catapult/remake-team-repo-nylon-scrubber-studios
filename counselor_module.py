import pygame
import random
import sys
import time
import button_module

class Counselor:
    def __init__(self,screen, movement_type,location,time_delay,difficulty):
        self.screen = screen
        self.movenment_type = movement_type
        self.location = location
        self.time_delay = time_delay
        self.difficulty = difficulty
        self.path = []
        self.times_ran = 0
        self.running = False
    def movement(self):
        milli_seconds = pygame.time.get_ticks()
        seconds = milli_seconds//1000-self.times_ran
        #checks if the animatronic is Carp
        if self.movenment_type == 'carp':
            #Carp's movement path
            self.path = ["livingroom","left_hallway","restroom","peek","left_doorway"]
            print(seconds)
            #if carp has stayed in his location for as long as his movement time
            if seconds == self.time_delay:
                #subtracts 5 seconds from seconds to prevent rerunning until next 5 seconds
                self.times_ran +=5
                movement_chance = random.randint(1,20)
                #return carp to his starting location if he has finished his path
                if self.location == 4:
                    self.location = 0
                #if carp as succeeded his movement chance
                if movement_chance <= self.difficulty:
                    #move to next position in list
                    self.location = self.location+1
                    #return his new location
                    return self.path[self.location]
                
            # if cou failed his movement chance, he stays where he was
            return self.path[self.location]

        if self.movenment_type == 'jj':
            #Checks if JJ is running
            if self.running == True:
                print(seconds)
                if seconds == 5:
                    self.location = self.location +1
                    self.running = False
                    return self.location
                else:
                    return 'running'


            self.path = ["kitchen(start)","kitchen(middle)","kitchen(end)","left_door"]
            print(seconds)
            #if carp has stayed in his location for as long as his movement time
            if seconds == self.time_delay:
                #subtracts 5 seconds from seconds to prevent rerunning until next 5 seconds
                self.times_ran +=5
                movement_chance = random.randint(1,20)
                #return carp to his starting location if he has finished his path
                if self.location == 3:
                    self.location = 0
                #if carp as succeeded his movement chance
                if movement_chance <= self.difficulty:
                    if self.location == 2:
                        self.running = True
                        print('Its Funishment Time')
                        print(self.running)
                        return 'running'
                        #pygame.mixer.Sound("its_funishment_time.wav").play()
                        
                        
                    #move to next position in list
                    self.location = self.location+1
                    #return his new location
                    return self.path[self.location]
                
            # if failed his movement chance, he stays where he was
            return self.path[self.location]
        

        if self.movenment_type == 'andrew':
            #Carp's movement path
            self.path = ["stairway","kitchen","right_hall_far","right_hall_close","right_doorway"]
            print(seconds)
            #if carp has stayed in his location for as long as his movement time
            if seconds == self.time_delay:
                #subtracts 5 seconds from seconds to prevent rerunning until next 5 seconds
                self.times_ran +=5
                movement_chance = random.randint(1,20)
                #return carp to his starting location if he has finished his path
                if self.location == 4:
                    self.location = 0
                #if carp as succeeded his movement chance
                if movement_chance <= self.difficulty:
                    #move to next position in list
                    self.location = self.location+1
                    #return his new location
                    return self.path[self.location]
                
            # if cou failed his movement chance, he stays where he was
            return self.path[self.location]

    def carp_button_pushed(self,button):
        if self.location > 2:
            self.location = 0

    def get_counselor(self):
        return self.path[self.location]



def main():
    pygame.init()
    pygame.display.set_caption("One Night at Catapult")
    screen = pygame.display.set_mode((800,600))
    carp_button = button_module.Buttons(screen,50,400,"images/button_test.png")

    # let's set the framerate

    carp = Counselor(None,'carp',2,5,20)
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if carp_button.is_pressed(pygame.mouse.get_pos()) == True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    carp.carp_button_pushed(carp_button)

        

        

        screen.fill((255, 255, 255))
        carp_button.draw()
    
    
    
        
        carp.movement()
        pygame.display.update()
if __name__ == '__main__':
    main()
