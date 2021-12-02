# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 10:18:55 2020

@author: Judith
"""
import numpy as np

with open("C:\\Users\\Judith\\Documents\\AdventForCode\\day10_input.txt", "r") as file:
    inputlst = file.readlines()
    inputlst = [int(line.strip()) for line in inputlst]
    
sorted_nr = sorted(inputlst)
diff = list(np.diff(sorted_nr))

print(min(inputlst))
nr_1 = diff.count(1)
nr_3 = diff.count(3) + 1
if int(min(inputlst)) == 1:
    nr_1 += 1
else:
    nr_3 += 1
print(f"Number of 1 joltage differences is {nr_1} and of 3 joltage differences is {nr_3}. The product of both is {nr_1*nr_3}")

#%%
#--------------------------------------
# Python program to print all 
# subset combination of n  
# element in given set of r element . 
  
# arr[] ---> Input Array 
# data[] ---> Temporary array to  
#             store current combination 
# start & end ---> Staring and Ending  
#                  indexes in arr[] 
# index ---> Current index in data[] 
# r ---> Size of a combination  
#        to be printed  
def combinationUtil(arr, n,
                    index, data, i, counter): 
    # Current combination is  
    # ready to be printed, 
    # print it 
    if(index == n - 1): 
        counter +=1
        #for j in range(r): 
            #print(data[j], end = " ") 
        #print(" ") 
        return
  
    # When no more elements  
    # are there to put in data[] 
    if(i >= n): 
        return
  
    # current is included,  
    # put next at next 
    # location  
    if (arr[i] - data[index - 1]) == 1 or (arr[i] - data[index - 1]) == 3:
        data[index] = arr[i] 
        combinationUtil(arr, n, index + 1, data, i + 1, counter) 
      
    # current is excluded,  
    # replace it with 
    # next (Note that i+1  
    # is passed, but index  
    # is not changed) 
    combinationUtil(arr, n, index,  
                    data, i + 1, counter) 
  
  
# The main function that 
# prints all combinations 
# of size r in arr[] of  
# size n. This function  
# mainly uses combinationUtil() 
def printcombination(arr, n, counter): 
  
    # A temporary array to 
    # store all combination 
    # one by one 
    data = list(range(r)) 
      
    # Print all combination  
    # using temporary  
    # array 'data[]' 
    combinationUtil(arr, n, 
                    0, data, 0, counter) 
  
  
# Driver Code 
arr = [28,
33,
18,
42,
31,
14,
46,
20,
48,
47,
24,
23,
49,
45,
19,
38,
39,
11,
1,
32,
25,
35,
8,
17,
7,
9,
4,
2,
34,
10,
3] 
arr = sorted(arr)
  
n = len(arr) 
counter = 0
printcombination(arr, n, counter) 
  
# This code is contributed 
# by Ambuj sahu 
