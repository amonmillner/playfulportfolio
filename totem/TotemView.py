# -*- coding: utf-8 -*-
"""
Created April 2019

@author: Amon Millner

This is a module that contains a class that serves as a view
for the totem game, to evoke the Model-View-Controller (MVC) framework.
"""

import pygame
from pygame.locals import *
import random


class TotemView(object):
    """ A view of Face Totem rendered in a Pygame window """
    def __init__(self, model, size, faces_list):
        """ Initialize the view with a reference to the model and the
            specified game screen dimensions (represented as a tuple
            containing the width and height).
            Keeps a list of the images available to render.
            It sets up the messages to display for the user.
        """
        self.model = model
        self.screen = pygame.display.set_mode(size)
        self.faceImages = []
        for face in faces_list: #puts images of all available faces in a list
            self.faceImages.append(pygame.image.load('faces/'+face))
        for i in range(len(self.faceImages)): #scales the images to 80 x 80
            self.faceImages[i] = pygame.transform.scale(self.faceImages[i],(80,80))
        self.my_font = pygame.font.SysFont('Comic Sans MS', 32)
        self.text_playing = self.my_font.render('press spacebar to stack heads',
                                              False, (200,200,200))
        self.text_won = self.my_font.render('You Win! Press Enter to play again'
                                             , False, (127,255,63))


    def draw(self):
        """ Draw the current game state to the screen """
        self.screen.fill(pygame.Color(63,63,63)) #makes a grey screen
        #iterates through faces in the model to draw them to the screen
        self.screen.blit(self.faceImages[self.model.face.face_index],
                         (self.model.face.x, self.model.face.y))
        #iterates through a dictionary that tracks where heads are on each level
        for key, value in self.model.foundation.items():
            self.screen.blit(self.faceImages[value.face_index], (value.x,
                                            value.y))
        #displays instructions to use spacebar to play
        if self.model.won_game == 0:
            self.screen.blit(self.text_playing, (0,0))
        else: #shows a user the text after winning, to press enter to play again
            self.screen.blit(self.text_won, (0,0))
            self.model.won_game = 0
            self.model.new_game = 1
        pygame.display.update()
