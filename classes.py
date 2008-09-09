# -*- coding: utf-8 -*-
import string
import sys
import math

import pygame
from pygame.locals import *

from utils import load_image
from config import *
 
class Label(pygame.sprite.Sprite):

    def __init__(self, text="", xy=(0,0), size=25, color=BLACK):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.size = size
        self.x, self.y = xy    #topleft
        self.color = BLACK
        self.image = pygame.Surface((self.size, self.size))

    def update(self):
        font = pygame.font.Font(None, self.size)
        self.image = font.render(self.text, True, self.color)
        self.rect = self.image.get_rect().inflate(10,10).move(self.x, self.y)


class App(object):

    def __init__(self, screen, cuerdas):
        self.cuerdas = cuerdas
        self.screen = screen
        self.load_bg()
        self.draw_cuerdas()
        self.widgets = pygame.sprite.OrderedUpdates()
        #self.widgets.add()
        #labels = [Label(u"(para transmisión digital)", (530, 380)), Label(u"(para transmisión analógica)", (530, 580))]
        #self.widgets.add(labels)
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
            image = font.render(str(i), True, BLACK)
            self.bg.blit(image, (x, y))
            ox,oy = x + 20, y + 10
            dx = ox + C*c
            dy = oy 
            pygame.draw.line(self.bg, BLACK, (ox,oy), (dx,dy), 3)
            y += 20

    def loop(self):
       pygame.display.flip()
       while not self.exit:

            self.clock.tick(100)
            
            self.screen.blit(self.bg, (0,0))
            
            for event in pygame.event.get():
                self.control(event)
            
            self.update()
            self.draw()
            
            pygame.display.flip()
            
    def control(self, event):
        if event.type == QUIT:
            sys.exit(0)
        elif event.type == KEYDOWN:
            self.keypress(event)
        elif event.type == MOUSEBUTTONDOWN:
            self.mouseclick(event) 
        
    def update(self):
        self.widgets.update()
        
    def mouseclick(self, event):
        pass
            
    def keypress(self, event):
        pass
        
    def draw(self):
        self.widgets.draw(self.screen)

if __name__ == '__main__':
    
    App().loop()

