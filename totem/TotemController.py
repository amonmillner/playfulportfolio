# -*- coding: utf-8 -*-
"""
Created April 2019

@author: Amon Millner

This is a module that contains a class that serves as a controller
for the totem game, to evoke the Model-View-Controller (MVC) framework.
"""

import pygame
from pygame.locals import *


class TotemController(object):
    """ Handles keyboard input for face stacker """
    def __init__(self,model):
        self.model = model

    def handle_event(self,event):
        """ Space key stops the moving faces """
        if event.type != KEYDOWN:
            return
        if event.key == pygame.K_SPACE:
            self.model.addFaceToFoundation()
        # making the enter key only reset after a victory
        if (self.model.new_game == 1 and event.key == pygame.K_RETURN):
            self.model.reset_game = 1
