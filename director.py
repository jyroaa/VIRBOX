# -*- encoding: utf-8 -*-

# M�dulos
import pygame
import confi
from time import sleep
class Director:
    """Representa el objeto principal del juego.

    El objeto Director mantiene en funcionamiento el juego, se
    encarga de actualizar, dibuja y propagar eventos.

    Tiene que utilizar este objeto en conjunto con objetos
    derivados de Scene."""

    def __init__(self):
        self.screen = pygame.display.set_mode((confi.width, confi.height))#,pygame.FULLSCREEN)
        pygame.display.set_caption(confi.name)
        self.scene = None
        self.fullscreen = False
        self.quit_flag = False
        self.clock = pygame.time.Clock()

    def loop(self):
        """Pone en funcionamiento el juego."""
            
        while not self.quit_flag:
            self.time = self.clock.tick(60)
            
            # Eventos de Salida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                
            # detecta eventos
            self.scene.on_event()

            # actualiza la escena
            self.scene.on_update()

            # dibuja la pantalla
            self.scene.on_draw(self.screen)
            pygame.display.flip()

    def change_scene(self, scene):
        """Altera la escena actual."""
        self.scene = scene

    def quit(self):
        self.quit_flag = True

