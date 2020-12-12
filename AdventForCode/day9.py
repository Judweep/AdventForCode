# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:34:25 2020

@author: Judith
"""

from itertools import combinations

with open("C:\\Users\\Judith\\Documents\\AdventForCode\\day9_input.txt", "r") as file:
    input = file.readlines()
    input = [int(line.strip()) for line in input]
    
def check_nr(current_nrlist, current_nr):
    for pair1, pair2 in combinations(current_nrlist,2):
        if pair1 + pair2 == current_nr:
            return None
    return current_nr

"""
for step_nr, nr in enumerate(range(25, len(input))):
    current_nrlist = input[:nr]
    current_nr = input[nr]
    not_valid = check_nr(current_nrlist, current_nr)
    if not_valid:s
        index= nr
        not_valid_nr = not_valid
        print(f"First number not valid: {not_valid} with index {nr}")
        break
    current_nrlist.pop(0)
    current_nrlist.append(input[nr])
"""
#%%
for i in range(index):
    subsequent_nrlist = [input[i]]
    counter = 0
    while sum(subsequent_nrlist) <= not_valid_nr:
        counter += 1
        subsequent_nrlist.append(input[i + counter])
        if sum(subsequent_nrlist) == not_valid_nr:
            min_nr = min(subsequent_nrlist)
            max_nr = max(subsequent_nrlist)
            print(f"List is {subsequent_nrlist}, {min_nr}, {max_nr}, {max_nr + min_nr}")
            break
        
        