import pygame

class PacMan(pygame.sprite.Sprite):
    def __init__(self,game,centerx,centery):
        super().__init__()
        self.game = game
        
        self.enemigos_anima = []
        
        for i in range(25): #Cargue de los 25 pacmans
            file = f'pacman{i}.png'
            img = pygame.image.load(file).convert()
            img.set_colorkey((255,255,255))
            self.enemigos_anima.append(img)
            
        self.image = self.enemigos_anima[1] ## Imagen por defecto
        self.rect = self.image.get_rect() #Para las colisiones
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.pulsada = 'right' # Tecla a la derecha por defecto
        self.orientacion = 1 # A la derecha por defecto
        
        self.orientacion_max = self.orientacion + 6
        self.vel_x=2 # Si se mueve ene x no se debe mover en y porq iria en diagonal.
        self.vel_y=0
        
        