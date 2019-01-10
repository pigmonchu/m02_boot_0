import pygame, sys
from pygame.locals import *
 
class App:
    '''
    Constructor
    '''
    def __init__(self, weight, height, title="pygame window"):
        self._running = True
        self.__screen = None
        self.size = self.weight, self.height = weight, height
        self.title = title
        
        self.bg = pygame.image.load("assets/background.png")
        
        
 
    def on_init(self):
        try:
            pygame.init()
            self.__screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
            pygame.display.set_caption(self.title)
            self._running = True
            return True
        except:
            return False
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass
    
    def on_render(self):
        self.__screen.blit(self.bg, (0,0))
        pygame.display.flip()
    
    def on_cleanup(self):
        pygame.quit()
        sys.exit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
#            for event in pygame.event.get():
#                self.on_event(event)
#            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App(640, 480, "Carrera pygame")
    theApp.on_execute()
