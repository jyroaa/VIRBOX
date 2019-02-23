# -*- encoding: utf-8 -*-
 
import scene
import confi
import graphics
import imagen 
from random import randint
from time import sleep
import threading
import serial
import pygame

class SceneGame(scene.Scene):
    """Escena inicial del juego, esta es la primera que se carga cuando inicia"""        
        
    def __init__(self, director):
        scene.Scene.__init__(self, director)    
        
        self.mensaje,self.pos_msg=graphics.text("Elija el color que esta escrito", 700, 70,(247, 220, 111 ), 30)     
        self.back = graphics.load_image(confi.fonts+"fondoJuego.jpg")
        self.imagenes = ["rojo10","verde1","rojo1","verde2","rojo2","verde3","rojo3","verde4","rojo4","verde5","rojo5","verde6","rojo6","verde7","rojo7","verde8","rojo8","verde9","rojo9"]
        self.numRandonX = None
        self.numRandonY = None
        #self.Figures=[]
        self.Figures=None
        #self.ser = serial.Serial(port='', baudrate=9600)
        self.datoEnviar=''
        self.datoRecibido=''
        
            
                 
        
    def juego(self,image1=[]):
        self.Figures=imagen.colores(confi.fonts + image1[randint(0,18)])     
        self.numRandonX = randint(50,500)
        self.numRandonY = randint(10,500)   
        sleep(2)
            
    #def recibirDatosSerial(self):
    #    return self.ser.readline(1)    
           
    def on_update(self):        
        self.juego(self.imagenes)
    
    def on_event(self):
        pass
 
    def on_draw(self, screen):
        screen.blit(self.back, (0,0))          
        #screen.blit(self.Figures,(self.numRandonX,self.numRandonY)) 
        if self.Figures:
            screen.blit(self.Figures.obtener_imagen(),(self.numRandonX,self.numRandonY))
            
            
        
