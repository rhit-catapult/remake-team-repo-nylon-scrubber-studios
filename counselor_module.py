import pygame
import random

class Counselor_System:
    def __init__(self,screen, movement_type,location,time_delay,difficulty):
        self.screen = screen
        self.movenment_type = movement_type
        self.location = location
        self.time_delay = time_delay
        self.difficulty = difficulty
        self.last_moved = 0
    def movement(self):
        if self.movenment_type == 'Carp':
            carp_path = [0,1,2,3,4]
            if self.last_moved == self.time_delay:
                movement_chance = random.randint(1,20)
                if self.location == 5:
                    self.location = 0
                if movement_chance > self.difficulty:
                    self.location = self.location+1
                    return carp_path[self.location]
                    

carp = Counselor_System(None,'Carp',0,0,10)
carp.movement()