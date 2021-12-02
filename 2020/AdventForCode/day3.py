
import numpy

input = open("C:\\Users\\Judith\\Documents\\AdventForCode\\day3_input.txt", "r"). readlines()
map = [line[:-1] for line in input]
rules = [1,3,5,7,1]
steps = [0,0,0,0,0]
trees = [0,0,0,0,0]
skip = True
for row in map:
    #Check for trees
    for nr,step in enumerate(steps):
        skip = not skip
        if nr == 4 and skip == True:
            break
        if row[step] == "#":
            trees[nr] += 1
       #Uptake step counter   
        steps[nr] = (steps[nr] + rules[nr])%len(row)
        

print(f"On his way through the forest he will encounter {*trees} trees.")
prodtrees = numpy.prod(trees,dtype = "uint")
print(f"The product of them is {prodtrees}")