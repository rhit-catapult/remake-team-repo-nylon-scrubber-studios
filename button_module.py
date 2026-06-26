
class Button:
    def __init__(self, screen,x,y,image,function):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.in_camera = bool
        self.button_pushed = bool
        self.function = function
    def draw(self):
        if self.in_camera == True:
            return
        self.screen.blit(self.image,(self.x,self.y))

    #determine if button was pushed
    def button_down(self):
        self.button_pushed = True
    def button_up(self):
        self.button_pushed = False

    #determine what the button will do if pushed
    def function(self):
        if self.button_pushed == False:
            #will not run if button was not pushed
            return
        if self.function == 'door':
            #will close door if button was pushed
            door_open = False
        elif self.function == 'camera':
            #will open cameras if button pushed
            camera_up = True
        elif self.function == 'aimen':
            #reset aimen clock
            aimen_time = 20