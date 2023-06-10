import pygame
import random
import sys
from clase_pacman import *
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
        
    def crearPantalla(self):
        pass
    
    def new_game(self):
        self.puntos_inicio = 0
        self.nivel = 1
        self.vidas = 3
        self.pacman = PacMan(self,25,25)
        self.lista_sprites_adibujar.add(self.pacman)
        
        
    def validar_nivelsuperado(self):
        pass
    
    def pausa_nivelsuperado(self):
        pass
    
    def update(self):
        self.lista_sprites_adibujar.update()
        
        
        pygame.display.flip()
        self.reloj.tick(self.FPS)
    
    def draw(self):
        self.pantalla.fill(self.GRIS_FONDO)
        
        self.lista_sprites_adibujar.draw(self.pantalla)
    
    def check_si_instancia_otro_pacman(self):
        pass
    
    def check_event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN and self.gameover:
                if pygame.K_KP_ENTER:
                    self.gameover=False
                    self.new_game()
                    self.run()
            elif not self.gameover:
                self.pacman.leer_teclado()
    def  run(self):
        while not self.gameover:
            self.check_event()
            self.update()
            self.draw()
        while self.gameover:
            self.update()
            self.draw()
            self.check_event()
            
if __name__=='__main__':
    game=Game()#Instanciamos la clase, es decir creamos el objeto
    game.run()