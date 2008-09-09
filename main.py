import sys
from classes import *

import pygame
from pygame.locals import *

from config import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def main():
    #Initialize
    pygame.init()
    screen = pygame.display.set_mode(WINDOW)
    #screen.fill(WHITE)
    pygame.display.set_caption(WINDOW_TITLE)

    cuerdas = (5, 10, 15, 30, 50, 65)

    app = App(screen, cuerdas)
    app.loop()

if __name__ == "__main__":
    main()
