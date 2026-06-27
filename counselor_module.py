import pygame
import random
import time

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
            #Carp's movement path
            if self.running == True:
                print(seconds)
                if seconds == self.time_delay+5:
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
                
            # if cou failed his movement chance, he stays where he was
            return self.path[self.location]


    def get_counselor(self):
        return self.path[self.location]



def main():
    jj = Counselor(None,'jj',2,5,20)
    clock = pygame.time.Clock()
    end = 0
    while True:
        clock.tick(60)
        print(jj.movement())
        if end == 600:
            break
        else:
            end+=1
if __name__ == '__main__':
    main()
