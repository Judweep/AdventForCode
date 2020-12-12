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
    def __init__(location, direction):
        ship.n, ship.e, ship.s, ship.w = location
        ship.location = (ship.n, ship.e, ship.s, ship.w)
        ship.direction = direction
    
    def move(action, value):
        if action == "N":
            ship.n += value
        elif action == "E":
            ship.e += value
        elif action == "S":
            ship.s += value
        elif action == "W":
            ship.w += value
        elif action == "L":
            ship.direction = (ship.direction - (value / 90)) % 4
        elif action == "R":
            ship.direction = (ship.direction + (value / 90)) % 4
        elif action == "F":
            ship.location[ship.direction] += value
        else:
            print("Error")
            

ferry = ship([0,0,0,0], 1)
for action, value in inputlst:
    ferry.move(action, value)