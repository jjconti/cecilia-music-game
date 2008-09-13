# -*- coding: utf-8 -*-
import string
import sys
import math
import time

import pygame
from pygame.locals import *

from utils import load_image, load_sound
from config import *

class Play(object):

    def __init__(self, screen, bg, cancion=None, cuerdas=None):
        self.cancion = cancion
        self.sounds = [load_sound(s) for s in SOUNDS]
        self.screen = screen
        self.screen.blit(bg, (0,0))
        self.exit = False
        self.clock = pygame.time.Clock()

    def play(self):
        pygame.display.flip()
        if self.cancion:
            self.cancion.play()
        while not self.exit:

            self.clock.tick(100)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == KEYDOWN:
                    self.exit = True

class Level(object):

    def __init__(self, screen, cuerdas, cancion, cancionwav, next):
        self.cuerdas = cuerdas
        self.sounds = [load_sound(s) for s in SOUNDS]
        self.cancion = []   #hasta 16 cuerdas
        self.cancionwav = cancionwav
        self.objetivo = cancion
        self.screen = screen
        self.load_bg()
        self.next = next
        self.draw_cuerdas()
        self.exit = False
        self.clock = pygame.time.Clock()

    def load_bg(self):
        fondo = load_image(FONDO)
        #porta = load_image(PORTA)
        #playbg = load_image(PLAYBG)
        self.bg = pygame.Surface(WINDOW)
        self.bg.blit(fondo, (0,0))
        #self.bg.blit(porta, (0,340))
        #self.bg.blit(playbg, (500,340))

    def draw_cuerdas(self):
        font = pygame.font.Font(None, 20)
        y = 340 + 15
        x = 15
        for i,c in enumerate(self.cuerdas):
            image = font.render(str(i+1),True, BLACK)
            self.bg.blit(image, (x, y))
            ox,oy = x + 20, y + 10
            dx = ox + C * CUERDAS[c]
            dy = oy 
            pygame.draw.line(self.bg, BLACK, (ox,oy), (dx,dy), 3)
            y += 20

    def draw_cancion(self):
        medio = 640 / 2
        y = 20
        for c in self.cancion:
            longi = C*CUERDAS[c]*1.5
            ox,oy = medio - longi / 2, y 
            dx = ox + longi
            dy = oy 
            pygame.draw.line(self.screen, BLACK, (ox,oy), (dx,dy), 5)
            y += 20

    def loop(self):
       pygame.display.flip()
       while not self.exit:

            self.clock.tick(100)
            
            self.screen.blit(self.bg, (0,0))
            self.draw_cancion()
            
            for event in pygame.event.get():
                self.control(event)

            if self.done():
                self.screen.blit(self.next, (0,0))
                pygame.display.flip()
                pygame.time.delay(2000)
                return

            pygame.display.flip()
            
    def control(self, event):
        if event.type == QUIT:
            sys.exit(0)
        elif event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if self.cancion:
                    self.cancion.pop()
            elif event.key == K_SPACE:
                self.cancionwav.stop()
                self.cancionwav.play()
            else:
                if event.unicode in (u"p", u"P"):
                    self.cancionwav.stop()
                else:
                    self.keypress(event)
        
    def done(self):
        return self.cancion ==  self.objetivo

    def keypress(self, event):
        if len(self.cancion) == 16:
            print "MAX cancion"
            return
        if event.unicode == u"1" and len(self.cuerdas) >= 1:
            self._cuerda(1)
        elif event.unicode == u"2" and len(self.cuerdas) >= 2:
            self._cuerda(2)
        elif event.unicode == u"3" and len(self.cuerdas) >= 3:
            self._cuerda(3)
        elif event.unicode == u"4" and len(self.cuerdas) >= 4:
            self._cuerda(4)
        elif event.unicode == u"5" and len(self.cuerdas) >= 5:
            self._cuerda(5)
        elif event.unicode == u"6" and len(self.cuerdas) >= 6:
            self._cuerda(6)

    def _cuerda(self, i):
        self.cancion.append(self.cuerdas[i - 1])
        self.sounds[i].play()

if __name__ == '__main__':
    
    App().loop()

