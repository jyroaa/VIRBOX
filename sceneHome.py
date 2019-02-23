import scene
import confi
import graphics
import pygame
import sceneGame
 
class SceneHome(scene.Scene):
    """Escena inicial del juego, esta es la primera que se carga cuando inicia"""
    
    def __init__(self, director):
        scene.Scene.__init__(self, director)        
        self.mensaje,self.pos_msg=graphics.text("Bienvenido a tu pausa activa ", 700, 70,(247, 220, 111 ), 100)
        self.continuar=pygame.transform.scale(graphics.load_image(confi.fonts+"continuar1.png"),(150, 50))          
        self.back = graphics.load_image(confi.fonts+"fondo1.jpg")
        self.titulo = pygame.transform.scale(graphics.load_image(confi.fonts+"bienvenido.jpg"),(900, 150))
        self.beneficios = pygame.transform.scale(graphics.load_image(confi.fonts+"beneficios.jpg"),(700,540))
        self.escudo = pygame.transform.scale(graphics.load_image(confi.fonts+"ud.jpg"),(75,75))
        self.logo = pygame.transform.scale(graphics.load_image(confi.fonts+"vrbox.jpg"),(150,150))
        
        self.scene_game=sceneGame.SceneGame(director)#cambiar de escena 
    def on_update(self):
        pass
 
    def on_event(self):
        if pygame.mouse.get_pressed()[0]:
            self.director.change_scene(self.scene_game)
        
 
    def on_draw(self, screen):
        screen.blit(self.back, (0,0))
        #screen.blit(self.titulo,(200,10))
        screen.blit(self.beneficios,(100,170))
        screen.blit(self.escudo,(1200,10))
        screen.blit(self.logo,(10,10))
        screen.blit(self.continuar,(1100, 670))
        screen.blit(self.mensaje,self.pos_msg)
        
