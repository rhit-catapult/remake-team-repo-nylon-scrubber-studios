import pygame
import sys
import button_module

class Start_Screen:
    def __init__(self, screen):
        self.screen = screen
        self.title_screen_font = pygame.font.SysFont("times new roman", 50, True, True)
        self.title_screen_text = self.title_screen_font.render("FOUR NIGHTS AT CATAPULT", True, (200,0,0))
        self.title_text_x = (self.screen.get_width() - self.title_screen_text.get_width())/2
        self.start_button = button_module(self.screen, 400, 300, "images/button_test.png")
    def draw_start_screen(self, title_text_y):
        self.screen.fill((0,0,0))
        self.screen.blit(self.title_screen_text, (self.title_text_x, title_text_y))
        self.start_button.draw()
        self.start_button.is_pressed()
        

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    test = Start_Screen(screen)
    while True:
        test.draw_start_screen(100)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    main()
    