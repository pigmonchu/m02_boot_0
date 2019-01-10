import pygame
from pygame.locals import *
import sys

class Turtle(pygame.sprite.Sprite):
    
    

class Race():
    def __init__(self, width, height):
        self.__size = (width, height)
        self.__title = "Carrera automática"
        
        self.background = pygame.image.load("assets/background.png")
            

    def launch(self):
        pygame.init()
        self.__screen = pygame.display.set_mode(self.__size, pygame.HWSURFACE)
        pygame.display.set_caption(self.__title)
        
        winner = False
        
        while not winner:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.__screen.blit(self.background, (0,0))
            pygame.display.flip()
        
        
if __name__ == '__main__':
    pygame.init()
    game = Race(640, 480)
    game.launch()
    