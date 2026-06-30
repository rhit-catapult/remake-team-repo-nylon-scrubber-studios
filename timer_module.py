import pygame
import sys

from settings import *

class Timer:
    def __init__(self,screen: pygame.Surface,x,y,image: str,scale_x,scale_y,time_length_ms):
        self.screen = screen
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(scale_x,scale_y))
        self.x = x
        self.y = y
        self.time_length = 360000
        self.timer_font = pygame.font.SysFont("Courier new",20,True)
        self.timer_text = ""
        self.win_condition = False

    def reset_clock(self):
        self.time_length = 360000

    def draw(self):
        self.screen.blit(self.image,(self.x,self.y))
        seconds_left = self.time_length//1000
        hour = 12
        if seconds_left > 600:
            hour = 12
        elif seconds_left > 480:
            hour = 1
        elif seconds_left > 360:
            hour = 2
        elif seconds_left > 240:
            hour = 3
        elif seconds_left > 120:
            hour = 4
        elif seconds_left > 0:
            hour = 5
        else:
            pygame.mixer.Sound('sounds/victory.wav').play()
            self.win_condition = True
        self.timer_text = self.timer_font.render(f"{hour:02}:00",False,(255,255,255))
        self.screen.blit(self.timer_text,(self.x+20,self.y+18))