'''
Created on 12.11.2011

@author: ezander
'''
import pygame
import os

class UI(object):
    def __init__(self, resdir):
        self.resdir = resdir

    def init(self):
        pygame.display.init()
        pygame.display.set_mode((640, 480))
        s = pygame.display.get_surface()
        main = pygame.image.load(os.path.join(self.resdir, 'main.png'))
        s.blit(main, (0, 0))
        pygame.display.flip()
        self.s = s

    def quit(self):
        pygame.quit()
