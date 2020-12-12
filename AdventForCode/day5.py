import math
import numpy

with open("C:\\Users\\Judith\\Documents\\AdventForCode\\day5_input.txt", "r") as file:
    input = file.readlines()

seatlst = [line.strip() for line in input]

def seatid(seatstr):
    # Row
    rowstr = seatstr[:7]
    row_lower = 0
    row_upper = int(math.pow(2,len(rowstr)) -1)
    for letter in rowstr:
        if letter == "F":
            row_upper -= ((row_upper - row_lower) // 2) + 1
        else:
            row_lower += math.ceil((row_upper - row_lower) / 2)
    row = row_lower

    rowbit = rowstr.replace("F", "0")
    rowbit = rowbit.replace("B", "1")
    row_bin = int(rowbit,2)

    # Col
    colstr = seatstr[7:]
    col_lower = 0
    col_upper = int(math.pow(2,len(colstr)) -1)
    for letter in colstr:
        if letter == "L":
            col_upper -= ((col_upper - col_lower) // 2) + 1
        else:
            col_lower += math.ceil((col_upper - col_lower) / 2)
    col = col_lower

    colbit = colstr.replace("L", "0")
    colbit = colbit.replace("R", "1")
    col_bin = int(colbit,2)
    
    seatid = row * 8 + col
    seatid_bin = row_bin * 8 + col_bin
    #return row, col, seatid, row_bin, col_bin, seatid_bin
    return seatid



# ---Part1---
seatidlst = [seatid(seat) for seat in seatlst]
max(seatidlst)

# ---Part2---
seatidlst_sorted = sorted(seatidlst)
seatidlst_sorted_diff = numpy.diff(seatidlst_sorted)
seatidlst_sorted[int(numpy.where(seatidlst_sorted_diff == 2)[0])]
bin(533)
# Find != 1 in list
# Find index - either reverse function or remember index