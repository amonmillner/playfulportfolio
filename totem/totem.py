# -*- coding: utf-8 -*-
"""
Created April 2019

@author: Amon Millner

This is an example game that presents players with
images of faces that bounce from wall to wall until
a player presses space to start or stack upon a totem
pole of faces. If the face misses the previously-stacked
faces, the game resets. If the player gets the totem
faces to stack to the top of the screen, they win.
"""

import pygame
import os
import sys
import time
from pygame.locals import *
from TotemView import *
from TotemModel import *
from TotemController import *

def walk_thru_images(dirname):
    """uses the OS package's walk function to capture the names of
    image files in the provided directory
    """
    image_names = []
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            image_names.append(filename)
    return image_names


if __name__ == '__main__':
    pygame.init()
    windowsize = (640, 480)
    model = TotemModel(windowsize)
    faces_list = walk_thru_images("faces")
    view = TotemView(model, windowsize, faces_list)
    controller = TotemController(model)

    while True: # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            controller.handle_event(event)
        model.update()
        if model.reset_game == 1: # remake classes with default values
            model = TotemModel(windowsize, len(faces_list)-1)
            view = TotemView(model, windowsize, faces_list)
            controller = TotemController(model)
            model.reset_game = 0
        view.draw()
        time.sleep(.001)
