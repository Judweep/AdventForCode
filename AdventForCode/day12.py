# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 21:01:39 2020

@author: Judith
"""

import numpy as np

with open("C:\\Users\\Judith\\Documents\\AdventForCode\\day12_input.txt", "r") as file:
    inputlst = file.readlines()
    inputlst = [(line[0],int(line.strip()[1:])) for line in inputlst]

# [N,E,S, W] = [0,1,2,3]

class ship():
    def __init__(self, location, direction):
        self.v, self.h = location
        #self.location = [self.v, self.h]
        self.direction = direction
    
    def move(self, action, value):
        if action == "N":
            self.v += value
        elif action == "E":
            self.h += value
        elif action == "S":
            self.v -= value
        elif action == "W":
            self.h -= value
        elif action == "L":
            self.direction = (self.direction - int(value / 90)) % 4
        elif action == "R":
            self.direction = (self.direction + int(value / 90)) % 4
        elif action == "F":
            if self.direction == 0:
                self.v += value
            elif self.direction == 1:
                self.h += value
            elif self.direction == 2:
                self.v -= value
            elif self.direction == 3:
                self.h -= value
            else:
                print("Error")
        else:
            print("Error")
    def locate(self, distance = True):
        if distance:
            return abs(self.v) + abs(self.h)
        else:
            return (self.v, self.h)
        
            

ferry = ship([0,0], 1)
for action, value in inputlst:
    ferry.move(action, value)
print(f"Ferry is here: {ferry.locate()} and moved {ferry.locate(distance = False)} units")
