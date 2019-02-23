# -*- coding: utf-8 -*-
 
"""M0dulo para implementar el manejo de graficos y superficies"""
 
# M�dulos
import pygame
 
# Carga una imagen transparencia y color tranasparente opcionales.
def load_image(filename, transparent=False, pixel=(0,0)):    
    try: image = pygame.image.load(filename)
    except pygame.error:
        raise SystemExit()
    image = image.convert()
    if transparent:
        color = image.get_at(pixel)
        image.set_colorkey(color, pygame.RLEACCEL)
    return image
 
def text(texto, posx, posy, color=(0, 0, 0), tam=25):    
    fuente = pygame.font.Font(None, tam)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect
