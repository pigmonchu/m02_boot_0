import sys
import pygame

class Game():
    
    def __init__(self, width, height):
        self.players = []
        self.size = (width, height)
        
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Carrera automática')
        
        self.background = pygame.image.load("assets/background.png").convert()
        
        
if __name__ == '__main__':
#    pygame.init()
    pygame.font.init()
    
    game = Game(640, 480)
    
            