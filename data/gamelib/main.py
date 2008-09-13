import sys

import pygame
from pygame.locals import *

from classes import *
from config import *
from utils import load_image

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def main():

    pygame.init()
    screen = pygame.display.set_mode(WINDOW)
    pygame.display.set_caption(WINDOW_TITLE)

    intro = load_image(INTRO)
    help = load_image(HELP)
    #final = load_image(FINAL)
    final2 = load_image(FINAL2)

    while True:

        Play(screen, intro).play()
        Play(screen, help).play()
        level1 = load_image(NEXT0)
        screen.blit(level1, (0,0))
        pygame.display.flip()
        pygame.time.delay(2000)

        cancionwav = None

        for level in LEVELS:
            bg = load_image(level['bg'])
            cuerdas = [int(x) for x in level['cuerdas']]
            cancion = [int(x) for x in level['cancion']]
            if cancionwav:
                cancionwav.stop()
            cancionwav = load_sound(level['wav'])
            next = load_image(level['next'])
    
            Play(screen, bg, cancionwav, cuerdas).play()
            lev = Level(screen, cuerdas, cancion, cancionwav, next)
            lev.loop()

        #Play(screen, final).play()
        Play(screen, final2).play()

if __name__ == "__main__":
    main()
