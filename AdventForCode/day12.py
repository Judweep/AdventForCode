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
        self.pos_v, self.pos_h = location
        #self.location = [self.pos_v, self.pos_h]
        self.dir_v, self.dir_h = direction
    
    def move(self, action, value):
        if action == "N":
            self.dir_v += value
        elif action == "E":
            self.dir_h += value
        elif action == "S":
            self.dir_v -= value
        elif action == "W":
            self.dir_h -= value
        elif action == "L":
            angle = int(value / 90)
            if angle == 1:
                self.dir_v, self.dir_h = self.dir_h, -self.dir_v
            elif angle ==2:
                self.dir_v, self.dir_h = -self.dir_v, -self.dir_h
            elif angle ==3:
                self.dir_v, self.dir_h = -self.dir_h, self.dir_v
            else:
                print("Error")
        elif action == "R":
            angle = int(value / 90)
            if angle == 1:
                self.dir_v, self.dir_h = -self.dir_h, self.dir_v
            elif angle ==2:
                self.dir_v, self.dir_h = -self.dir_v, -self.dir_h
            elif angle ==3:
                self.dir_v, self.dir_h = self.dir_h, -self.dir_v
            else:
                print("Error")
        elif action == "F":
            self.pos_v += value * self.dir_v
            self.pos_h += value * self.dir_h
        else:
            print("Error")
    def locate(self, distance = True):
        if distance:
            return abs(self.pos_v) + abs(self.pos_h)
        else:
            return (self.pos_v, self.pos_h)
        
            

ferry = ship([0,0], [1,10])
for action, value in inputlst:
    ferry.move(action, value)
print(f"Ferry is here: {ferry.locate()} and moved {ferry.locate(distance = False)} units")
