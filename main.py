import sys
from classes import *

import pygame
from pygame.locals import *

from config import *
from utils import load_image

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def main():
    #Initialize
    pygame.init()
    screen = pygame.display.set_mode(WINDOW)
    #screen.fill(WHITE)
    pygame.display.set_caption(WINDOW_TITLE)

    for level in LEVELS:
        cuerdas = [int(x) for x in level['cuerdas']]
        cancion = [int(x) for x in level['cancion']]
        
        bg = load_image(level['bg'])
        Play(screen, cancion, cuerdas, bg).play()
        lev = Level(screen, cuerdas, cancion)
        lev.loop()

if __name__ == "__main__":
    main()
