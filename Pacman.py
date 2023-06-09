import pygame
import random
import sys
#from pac1 import *
#from pac2 import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init() #Sonidos y musica
        
        #Colores del juego
        self.AMARILLO = (220,190,0)
        self.BLANCO = (240,240,240)
        self.GRIS_FONDO = (73,73,73)
        self.ROJO = (240,0,0)
        self.VERDE_FONDO = (0,255,0)
        
        self.gameover = True
        self.level_success = True
        

