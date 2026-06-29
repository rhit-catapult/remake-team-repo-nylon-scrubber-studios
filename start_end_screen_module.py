import pygame
import sys
import button_module

from settings import *

class Start_Screen:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.title_screen_font = pygame.font.SysFont("courier new", 50, True, True)
        self.start_screen_text = self.title_screen_font.render("FOUR NIGHTS AT CATAPULTS", True, (200,0,0))
        self.game_over_screen_text = self.title_screen_font.render("YOU GOT FUNISHED!", True, (200,0,0))
        self.start_screen_text_x = (self.screen.get_width() - self.start_screen_text.get_width())/2
        self.game_over_screen_text_x = (self.screen.get_width() - self.game_over_screen_text.get_width())/2
        self.start_button = button_module.Buttons(self.screen, 400, 300, "images/button_test.png")
        self.game_over_button = button_module.Buttons(self.screen, 400, 300, "images/button_test.png")

    def draw_start_screen(self, title_text_y):
        self.screen.fill((0,0,0))
        self.screen.blit(self.start_screen_text, (self.start_screen_text_x, title_text_y))
        self.start_button.draw()
        
    def draw_game_over_screen(self, title_text_y):
        self.screen.fill((0,0,0))
        self.screen.blit(self.game_over_screen_text, (self.game_over_screen_text_x, title_text_y))
        self.game_over_button.draw()
             
        

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    test = Start_Screen(screen)
    while True:
        # test.draw_start_screen(100)
        test.draw_game_over_screen(100)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if test.game_over_button.is_pressed(pygame.mouse.get_pos()):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print("returning to menu")
                # if test.start_button.is_pressed(pygame.mouse.get_pos()):
                    #event logic for mousebuttondown gives multiple
                    # if event.type == pygame.MOUSEBUTTONDOWN:
                        # print("START GAME LETTTSSSS GOOOOOOO YOOOOO YOOOO YOOOO")
                        # while True:
                        #     test.draw_game_over_screen(100)
                        #     if test.game_over_button.is_pressed(pygame.mouse.get_pos()):
                        #         if event.type == pygame.MOUSEBUTTONDOWN:
                        #             print("exited game")
                        #             break
        pygame.display.update()


if __name__ == "__main__":
    main()
    