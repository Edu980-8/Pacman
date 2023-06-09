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
        
        #------Banderas del Juego-------------------#
        self.gameover = True
        self.level_success = True
        self.pausa_superado_tomartiempo = pygame.time.get_ticks() #Cuando se supere el nivel va a haber una pausa de tiempo
        
        #-------------Tamaño personajes-------------#
        self.BSX = 50 #Tamaño de cada personaje del mapa fantasma( 50 x 50) y pacman (50 x 50).
        self.BSY = 50
        
        #------------Caracteristicas iniciales------#
        self.puntos_inicio = 0
        self.nivel_inicio = 1
        self.vidas = 3
        self.PAUSA_MUERTE = 2000
        self.res_pantalla = (1200,700) # Tamaño de la pantalla de juego
        self.FPS = 60 #
        
        #----------------------Creo la pantalla----------------------------#
        self.pantalla = pygame.display.set_mode(self.res_pantalla)
        pygame.display.set_caption("Pacman by EdDesign con machine Learning")
        self.reloj = pygame.time.Clock()
        
        
        #---------------------Listas de fantasmas y pacman----------------#
        self.lista_sprites_adibujar = pygame.sprite.Group() #Crea un grupo de sprites vacio para almacenar gestionar y manipular los sprites
        self.lista_pacman = pygame.sprite.Group()
        
        self.crearPantalla()
        
    def crearPantalla():
        pass
    
    def new_game(self):
        self.puntos_inicio = 0
        self.nivel = 1
        self.vidas = 3
        
    def validar_nivelsuperado(self):
        pass
    
    def pausa_nivelsuperado(self):
        pass
    
    
    