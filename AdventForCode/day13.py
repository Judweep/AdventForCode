# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 22:24:36 2020

@author: Judith
"""

with open("C:\\Users\\Judith\\Documents\\AdventForCode\\day13_input.txt", "r") as file:
    inputlst = file.readlines()
    
arrival = int((inputlst[0]))
timetable = inputlst[1].split(",")
busnr = [int(bus) for bus in inputlst[1].replace("x,", "").split(",")]

waittime = [bus - (arrival % bus) for bus in busnr]

shortest_waittime = min(waittime)
earliest_bus = busnr[waittime.index(min(waittime))]

print(f"Shortest waittime is {shortest_waittime} minutes for bus {earliest_bus}. Product is {shortest_waittime * earliest_bus}")
print(busnr)
print(waittime)
