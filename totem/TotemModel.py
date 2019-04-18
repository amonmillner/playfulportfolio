# -*- coding: utf-8 -*-
"""
Created April 2019

@author: Amon Millner

This is a module that contains a class that serves as a model
for the totem game built, which is an example of the
Model-View-Controller (MVC) framework.
"""
import pygame, copy
from pygame.locals import *
import random


class TotemModel(object):
    """ Encodes a model of the game state """
    def __init__(self, size=(640,480),number_of_faces=0):
        self.width, self.height = size
        self.level = 1
        self.foundation = {}
        self.direction = 'left'
        self.reset_game = 0
        self.won_game = 0
        self.new_game = 0
        self.number_of_faces = number_of_faces
        self.face_index = random.randint(0, number_of_faces)
        self.face = Face(self.width, self.height, self.face_index)


    def addFaceToFoundation(self):
        """Puts a face in the game area on the current level where
        the user pressed the space key. Future rows will check the location
        of faces in the foundation to test whether a head can stack on top.
        """
        if self.level > 1: #only initiates if there are faces below
            #compares the x and y values of the face below to check boundaries
            if (self.face.x > (self.foundation[self.level-1].x + (self.face.width//2)))\
            or ((self.face.x + (self.face.width//2)) < self.foundation[self.level-1].x):
                self.reset_game = 1 #sets the reset flag if out of bounds
                return
        self.oldface = copy.deepcopy(self.face) #puts a copy into the foundation
        self.foundation[self.level] = self.oldface
        self.level += 1
        #picks a new face from the array of possible images
        self.face_index = random.randint(0, self.number_of_faces)


    def update(self):
        """ Update the game state """
        if self.face.x > (self.width - self.face.width):
            self.direction = 'left'
        elif self.face.x < 1: # checks the left wall, changes direction
            self.direction = 'right'
        # checks to see whether the stack is high enough to win the game
        if (self.height - (self.face.height * self.level)) < self.face.height:
            self.won_game = 1
        else:
            # calls each face's update function, to help facilitate its drawing
            self.face.update(self.height - (self.face.height * self.level),
                                 self.direction, self.level, self.face_index)


    def __str__(self):
        output_lines = []
        # will detail each face as a string
        for key, value in self.foundation:
            output_lines.append(str(value))
        # print one item per line
        return "\n".join(output_lines)


class Face(object):
    """ Encodes the state of a face in the game """
    def __init__(self,starting_x=0,starting_y=0,velocity=6,height=80,width=80,
                 face_index=0):
        self.height = height
        self.width = width
        self.x = starting_x
        self.y = starting_y - self.height
        self.velocity = velocity
        self.face_index = face_index


    def update(self, vertLocation, direction, level, new_face_index):
        """ update the state of the faces """
        if direction == 'right':
            self.x += (self.velocity + (level)) # adds speed as level increases
        else:
            self.x -= (self.velocity + (level))
        self.y = vertLocation
        if self.face_index != new_face_index: #sets a new face upon level ups
            self.face_index = new_face_index


    def __str__(self):
        return "Face height=%f, width=%f, x=%f, y=%f, velocity=%f" % (self.height,
                                                          self.width,
                                                          self.x,
                                                          self.y,
                                                          self.velocity,
                                                          self.face_index)
