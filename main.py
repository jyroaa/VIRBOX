#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# M�dulos
import pygame
import director
import sceneGame
import sceneHome
 
def main():
   
    dir = director.Director()
    scene1 = sceneHome.SceneHome(dir)
    dir.change_scene(scene1)    
    scene2=sceneGame.SceneGame(dir)       
    dir.loop()  
 
if __name__ == '__main__':
    pygame.init()
    main()