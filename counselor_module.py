import pygame
import random
import time
import button_module
import sys
import office_module
import start_end_screen_module

class Counselor:
    def __init__(self,screen, movement_type,location: int,time_delay,difficulty,time):
        self.screen = screen
        self.movenment_type = movement_type
        self.location = location
        self.time_delay = time_delay
        self.difficulty = difficulty
        self.path = []
        self.times_ran = 0
        self.running = False
        self.jump_time_start =0
        self.kill_clock = 5
        self.kill = False
        self.seconds = 0
        self.last_start_time = time

    def reset(self):
        self.last_start_time = pygame.time.get_ticks()
        

    def movement(self,ethan=None):
        milli_seconds= pygame.time.get_ticks() - self.last_start_time
        print(milli_seconds)
        self.seconds= milli_seconds//1000-self.times_ran
        #checks if the animatronic is Carp
        if self.movenment_type == 'carp':
            #Carp's movement path
            self.path = ["livingroom","left_hallway","restroom","peek","left_doorway"]
            # print(self.path[self.location])
            #if carp has stayed in his location for as long as his movement time
            if self.seconds== self.time_delay:
                #subtracts 5 self.secondsfrom self.secondsto prevent rerunning until next 5 seconds
                self.times_ran += self.time_delay
                movement_chance = random.randint(1,20)
                if self.location == 4:
                    # print(pygame.time.get_ticks()//1000)
                    self.jump_time_start = pygame.time.get_ticks() + 5000
                    self.kill = True
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
            #Carp's movement path
            if self.running == True:
                # print(seconds)
                self.location = 3
                if self.seconds == 5:
                    # print(pygame.time.get_ticks()//1000)
                    self.jump_time_start = pygame.time.get_ticks() + 5000
                    self.kill = True
                    self.location = 0
                    self.running = False
                    return self.kill
                else:
                    return 'running'


            self.path = ["kitchen(start)","kitchen(middle)","kitchen(end)",'running']
            # print(seconds)
            #if carp has stayed in his location for as long as his movement time
            if self.seconds== self.time_delay:
                #subtracts 5 self.secondsfrom self.secondsto prevent rerunning until next 5 seconds
                self.times_ran +=5
                movement_chance = random.randint(1,20)
                #return carp to his starting location if he has finished his path
                #if carp as succeeded his movement chance
                if movement_chance <= self.difficulty:
                    if self.location == 2:
                        self.running = True
                        #pygame.mixer.Sound("its_funishment_time.wav").play()
                    else:
                        
                    #move to next position in list
                        self.location = self.location+1
                    #return his new location
                    return self.path[self.location]
                
            # if failed his movement chance, he stays where he was
            return self.path[self.location]
        

        if self.movenment_type == 'andrew':
            #Carp's movement path
            self.path = ["stairway","kitchen","right_hall_far","right_hall_close","right_doorway"]
            print(self.seconds)
            #if carp has stayed in his location for as long as his movement time
            if self.seconds== self.time_delay:
                #subtracts 5 self.secondsfrom self.secondsto prevent rerunning until next 5 seconds
                self.times_ran +=5
                movement_chance = random.randint(1,20)
                #return carp to his starting location if he has finished his path
                if self.location == 4:
                    # print(pygame.time.get_ticks()//1000)
                    self.jump_time_start = pygame.time.get_ticks() + 5000
                    self.kill = True
                    self.location = 0
                #if carp as succeeded his movement chance
                if ethan == self.path[self.location]:
                    self.location = self.location + 1
                    print(self.path[self.location])
                    return
                
                if movement_chance <= self.difficulty:
                    #move to next position in list
                    self.location = self.location+1
                    #return his new location
                    return self.path[self.location]
                
            # if failed his movement chance, he stays where he was
            return self.path[self.location]
    
    def carp_button_pushed(self):
        if self.location > 0 and self.location != 2:
            self.location = 0


    def ethan_movement(self):
        milli_seconds= pygame.time.get_ticks()
        self.seconds= milli_seconds//1000-self.times_ran
        if self.movenment_type == 'ethan':
            #Carp's movement path
            self.path = ["livingroom","kitchen","right_hall","left_hall","restroom"]
            print(self.seconds)
            #if carp has stayed in his location for as long as his movement time
            if self.seconds== self.time_delay:
                #subtracts 5 self.secondsfrom self.secondsto prevent rerunning until next 5 seconds
                self.times_ran +=5
                movement_chance = random.randint(1,20)
                #return carp to his starting location if he has finished his path
                #if carp as succeeded his movement chance




                if movement_chance <= self.difficulty:
                    #move to next position in list
                    self.location = random.randint(0,4)
                    #return his new location
                    return self.path[self.location]
                
            # if failed his movement chance, he stays where he was
            return self.path[self.location]

    
        
        
            
    def get_counselor(self):
        if self.movenment_type == 'carp':
            self.path = ["livingroom","left_hallway","restroom","peek","left_doorway"]
        if self.movenment_type == 'jj':
            self.path = ["kitchen(start)","kitchen(middle)","kitchen(end)",'running']
        if self.movenment_type == 'andrew':
            self.path = ["stairway","kitchen","right_hall_far","right_hall_close","right_doorway"]
        if self.movenment_type == 'ethan':
            self.path = ["livingroom","kitchen","right_hall","left_hall","restroom"]
        return self.path[self.location]


class Aimen:
    def __init__(self,timer):
        self.seconds= 0
        self.aimen_awake = False
        self.timer = timer
        self.start_time =0
        self.jump_time_start =0
        self.aiman_timer_font = pygame.font.SysFont("courier new", 20)
        self.aiman_timer_text = self.aiman_timer_font.render(f"{50-self.seconds}", False, "White", "Black")

    def aimen_clock(self):
        self.seconds= pygame.time.get_ticks()//1000 - self.start_time
        self.aiman_timer_text = self.aiman_timer_font.render(f"{50-self.seconds}", False, "White", "Black")
        if self.seconds>= self.timer and self.aimen_awake== False:
            self.jump_time_start = pygame.time.get_ticks() + 5000
            self.aimen_awake = True
        
    
    def aimen_button_pushed(self):
        self.start_time = pygame.time.get_ticks()//1000

def main():
    pygame.init()
    pygame.display.set_caption("One Night at Catapult")
    screen = pygame.display.set_mode((800,600))
    aimen_button = button_module.Buttons(screen,50,400,"images/button_test.png")

    # let's set the framerate
    andrew = Counselor(None,'andrew',0,5,20)
    ethan = Counselor(None,'ethan',0,5,1)
    aimen = Aimen(20)
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if aimen_button.is_pressed(pygame.mouse.get_pos()) == True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    aimen.aimen_button_pushed()

        

        

        screen.fill((255, 255, 255))
        aimen_button.draw()
        aimen.aimen_clock()
        ethan.movement()
        print(andrew.movement(ethan))

        pygame.display.update()
if __name__ == '__main__':
    main()
