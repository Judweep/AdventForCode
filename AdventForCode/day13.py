# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 22:24:36 2020

@author: Judith
"""

with open("C:\\Users\\Judith\\Documents\\AdventForCode\\day13_input_short.txt", "r") as file:
    inputlst = file.readlines()
    
arrival = int((inputlst[0]))
busnr = [int(bus) for bus in inputlst[1].replace("x,", "").split(",")]

waittime = [bus - (arrival % bus) for bus in busnr]

shortest_waittime = min(waittime)
earliest_bus = busnr[waittime.index(min(waittime))]

print(f"Shortest waittime is {shortest_waittime} minutes for bus {earliest_bus}. Product is {shortest_waittime * earliest_bus}")
print(busnr)
print(waittime)

#%%


timetable = [int(bus) if bus.isdigit() else bus for bus in inputlst[1].strip().split(",")]
bustimes = []
for index, busid in enumerate(timetable):
    if isinstance(busid, int):
        bustimes.append((busid, index))

for t in range(10000000000000000):
    if all([(t + offset) % busid == 0 for budid, offset in bustimes]):
        print(t)
        break