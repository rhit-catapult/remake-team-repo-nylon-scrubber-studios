import pygame
import sys
import button_module

from settings import *

class Start_Screen:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.start_screen_image = pygame.image.load("images/title_screen.png")
        self.start_screen_image = pygame.transform.scale(self.start_screen_image,(WINDOW_WIDTH,WINDOW_HEIGHT))
        self.title_screen_font = pygame.font.SysFont("courier new", 50, True, True)
        self.game_over_screen_text = self.title_screen_font.render("YOU GOT FUNISHED!", True, (200,0,0))
        self.win_screen_text = self.title_screen_font.render("YOU WON", True, (200,0,0))
        self.game_over_screen_text_x = (self.screen.get_width() - self.game_over_screen_text.get_width())/2
        self.win_screen_text_x = (self.screen.get_width() - self.game_over_screen_text.get_width())/2
        self.start_button = button_module.Buttons(self.screen, 250, 300, "images/play_button.png")
        self.game_over_button = button_module.Buttons(self.screen, 600, 300, "images/menu_button.png")
        self.win_button = button_module.Buttons(self.screen,100,300,"images/menu_button.png")

    def draw_start_screen(self):
        self.screen.blit(self.start_screen_image, (0,0))
        self.start_button.draw(280,120)
        
    def draw_game_over_screen(self, title_text_y):
        pygame.mixer.stop()
        self.screen.fill((0,0,0))
        self.screen.blit(self.game_over_screen_text, (self.game_over_screen_text_x, title_text_y))
        self.game_over_button.draw()

    def draw_win_screen(self,title_text_y):
        pygame.mixer.Sound('sounds/victory.wav').play()
        self.screen.fill((0,0,0))
        self.screen.blit(self.win_screen_text, (self.win_screen_text_x,title_text_y))
        self.win_button.draw()
             
        

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
    