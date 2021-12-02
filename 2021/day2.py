import numpy as np

dayNr = 2
with open(f"C:\\Users\\Judith\\Documents\\Programmieren\\AdventForCode\\2021\\input_day{dayNr}.txt", "r") as file:
    input = file.readlines()

#%% Part 1 ----------------

instructions = {"forward": 0, "down": 0, "up": 0}
for line in input:
    direction, value = line.split(" ")
    instructions[direction] += int(value)


print(instructions["forward"] * (instructions["down"] - instructions["up"] ))

#%% Part  2 --------------------
instructions = {"forward": 0, "depth": 0, "aim": 0}
for line in input:
    direction, value = line.split(" ")
    if (direction == "up"):
        instructions["aim"] -= int(value)
    elif (direction == "down"):
        instructions["aim"] += int(value)
    else:
        instructions["forward"] += int(value)
        instructions["depth"] += instructions["aim"] * int(value)

print(instructions["forward"] * instructions["depth"] )
