import pygame
import random
import time

class Counselor_System:
    def __init__(self,screen, movement_type,location,time_delay,difficulty):
        self.screen = screen
        self.movenment_type = movement_type
        self.location = location
        self.time_delay = time_delay
        self.difficulty = difficulty
        self.last_moved = 0
        self.path = []
        self.times_ran = 0
    def movement(self):
        milli_seconds = pygame.time.get_ticks()
        seconds = milli_seconds//1000-self.times_ran
        #checks if the animatronic is Carp
        if self.movenment_type == 'Carp':
            #Carp's movement path
            self.path = ["livingroom","left_hallway","restroom","peek","pos5"]
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
                if movement_chance > self.difficulty:
                    #move to next position in list
                    self.location = self.location+1
                    #return his new location
                    return self.path[self.location]
                
            # if cou failed his movement chance, he stays where he was
            return self.path[self.location]
        

        if self.movenment_type == 'JJ':
            #Carp's movement path
            self.path = ["kitchen(start)","kitchen(middle)","kitchen(end)","left door"]
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
                if movement_chance > self.difficulty:
                    #move to next position in list
                    self.location = self.location+1
                    #return his new location
                    return self.path[self.location]
                
            # if cou failed his movement chance, he stays where he was
            return self.path[self.location]


    def get_counselor(self):
        return self.path[self.location]
                    




carp = Counselor_System(None,'Carp',0,5,10)
clock = pygame.time.Clock()
end = 0
while True:
    clock.tick(60)
    print(carp.movement())
    if end == 300:
        break
    else:
        end+=1