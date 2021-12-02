import numpy as np
import time 

dayNr = 1
with open(f"C:\\Users\\Judith\\Documents\\Programmieren\\AdventForCode\\2021\\input_day{dayNr}.txt", "r") as file:
    input = file.readlines()
    heights = [int(line.strip()) for line in input]

    ## other solutions:
    # heights = list(map(int, input_file.readlines()))

#%% Part 1 ------------------------
diffHeights = np.diff(heights)
tic = time.perf_counter()
print(sum([diffHeight>0 for diffHeight in diffHeights]))
toc = time.perf_counter()
print(f"Calculated diffs in {toc - tic:0.4f} seconds")
tic = time.perf_counter()
print(np.count_nonzero(diffHeights>0)) # much faster
toc = time.perf_counter()
print(f"Calculated diffs in {toc - tic:0.4f} seconds")

## other solutions:
# print(sum([num > prev for prev, num in zip(heights, heights[1:])]))


#%% Part 2 ------------------------
diffSummedHeights = np.diff(np.convolve(heights,np.ones(3,dtype=int),'valid'))
print(np.count_nonzero(diffSummedHeights>0))



