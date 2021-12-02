
import os
import math
import numpy as np

# ----Day1-----

# Import expense report
report = open("C:\\Users\\Judith\\Documents\\AdventForCode\\day1_input.txt", "r").readlines()  
nrlist = [int(line[:-1]) for line in report] # Remove line breacks of every list entry

# ---Part 1--- Find two numbers that sum up to 2020 and take the product
sublist = [2020 - nr for nr in nrlist] # Create list with 2020 subtracted from the inital values
for subnr in sublist:
    if subnr in nrlist:
        nr1 = subnr
        nr2 = 2020 - nr1
        break
print(f"The numbers are {nr1} and {nr2}. The product of both is {nr1 *nr2}")

# ---Part 2--- Find three numbers that sum up to 2020 and take the product
for onr in nrlist:
    for subnr in sublist:
        if subnr - onr in nrlist:
            nr3 = subnr - onr
            nr4 = onr
            nr5 = 2020 - nr4 - nr3
            break
print(f"The numbers are {nr3}, {nr4} and {nr5}. The product of the three is {nr3 * nr4 * nr5}")
