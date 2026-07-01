import pygame
import sys
import button_module

from settings import *

class Start_Screen:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.start_screen_image = pygame.image.load("images/title_screen.png")
        self.start_screen_image = pygame.transform.scale(self.start_screen_image,(WINDOW_WIDTH,WINDOW_HEIGHT))
        self.win_screen_image = pygame.image.load("images/win_screen.png")
        self.win_screen_image = pygame.transform.scale(self.win_screen_image,(WINDOW_WIDTH,WINDOW_HEIGHT))
        self.game_over_image = pygame.image.load("images/game_over_screen.png")
        self.game_over_image = pygame.transform.scale(self.game_over_image,(WINDOW_WIDTH,WINDOW_HEIGHT))
        self.title_screen_font = pygame.font.SysFont("courier new", 25, True)
        self.transition_screen_image = self.title_screen_font.render("Night Starting!", True, (200,0,0))
        self.start_button = button_module.Buttons(self.screen, 250, 300, "images/play_button.png")
        self.game_over_button = button_module.Buttons(self.screen, 236, 450, "images/menu_button.png")
        self.win_button = button_module.Buttons(self.screen,236,400,"images/menu_button.png")
        self.difficulty_button = button_module.Buttons(self.screen,320,450, "images/difficulty_button.png")
        self.difficulty_slider = 1
        self.difficulty_number = self.title_screen_font.render(f"{self.difficulty_slider}",True,(0,0,0))
        

    def draw_start_screen(self):
        self.screen.blit(self.start_screen_image, (0,0))
        self.start_button.draw(280,120)
        self.difficulty_button.draw(140,60)
        self.difficulty_number = self.title_screen_font.render(f"{self.difficulty_slider}",True,(0,0,0))
        self.screen.blit(self.difficulty_number,(380,476))
        
    def draw_transition_screen(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.transition_screen_image,(WINDOW_WIDTH/2-self.transition_screen_image.get_width()/2,WINDOW_HEIGHT/2))


    def draw_game_over_screen(self):
        pygame.mixer.stop()
        self.screen.blit(self.game_over_image, (0,0))
        self.game_over_button.draw(328,120)

    def draw_win_screen(self):
        self.screen.blit(self.win_screen_image,(0,0))
        self.win_button.draw(280,120)
             
        

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    test = Start_Screen(screen)
    while True:
        # test.draw_start_screen(100)
        test.draw_start_screen()
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
    