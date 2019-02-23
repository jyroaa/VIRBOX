import pygame




class colores(pygame.sprite.Sprite):
    def __init__(self, texto):
        pygame.sprite.Sprite.__init__(self)       
        self.image = pygame.image.load(texto + ".png")        
        self.copia_imagen = self.image 
               
    
    def obtener_imagen(self):
        return self.copia_imagen

    def obtener_rect(self):
        return self.rect


    