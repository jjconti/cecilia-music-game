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

    def __init__(self, screen, cancion, cuerdas, bg):
        self.cancion = cancion
        self.cuerdas = cuerdas
        self.sounds = [load_sound(s) for s in SOUNDS]
        self.screen = screen
        self.screen.blit(bg, (0,0))

    def play(self):
        pygame.display.flip()
        for c in self.cancion:
            self.sounds[self.cuerdas.index(c) + 1].play()
            time.sleep(1)

class Level(object):

    def __init__(self, screen, cuerdas, cancion):
        self.cuerdas = cuerdas
        self.sounds = [load_sound(s) for s in SOUNDS]
        self.cancion = []   #hasta 18 cuerdas
        self.objetivo = cancion
        self.screen = screen
        self.load_bg()
        self.draw_cuerdas()
        self.widgets = pygame.sprite.OrderedUpdates()
        self.exit = False
        self.clock = pygame.time.Clock()

    def load_bg(self):
        fondo = load_image(FONDO)
        porta = load_image(PORTA)
        playbg = load_image(PLAYBG)
        self.bg = pygame.Surface(WINDOW)
        self.bg.blit(fondo, (0,0))
        self.bg.blit(porta, (0,340))
        self.bg.blit(playbg, (500,340))

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
            
            self.update()
            self.draw()
            
            pygame.display.flip()
            
    def control(self, event):
        if event.type == QUIT:
            sys.exit(0)
        elif event.type == KEYDOWN:
            if event.key == K_RETURN:
                if self.play():
                    self.exit = True
            elif event.key == K_ESCAPE:
                if self.cancion:
                    self.cancion.pop()
            else:
                self.keypress(event)
        elif event.type == MOUSEBUTTONDOWN:
            self.mouseclick(event) 
        
    def play(self):
        for c in self.cancion:
            self.sounds[c + 1].play()
            time.sleep(1)
        if self.cancion ==  self.objetivo:
            print "Ganaste!"
            return True
        else:
            print "Perdiste!"
            return False

    def update(self):
        self.widgets.update()

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

    def draw(self):
        self.widgets.draw(self.screen)

if __name__ == '__main__':
    
    App().loop()

