
# ----Day2----
input = open("C:\\Users\\Judith\\Documents\\AdventForCode\\day2_input.txt", "r").readlines()

# ---Part1---
nrlines = len(input)
n = 0
m = 0
for line in input:
    limit, letter, password = line.split(" ") # split line into three strings
    lower, upper = limit.split('-') # Split limit into lower and upper boundary
    lower, upper = int(lower), int(upper)
    letter = letter[0]
    if lower <= password.count(letter) <= upper: # Check if password is valid
        n += 1 # Increase counter for correct passwords
    if (password[lower-1] == letter and password[upper-1] != letter) or (password[lower-1] != letter and password[upper-1] == letter):
        m += 1

print(f"Out of {nrlines} passwords, {n} are valid accounting to the old policy.")
print(f"Out of {nrlines} passwords, {m} are valid accounting to the new policy.")

# ---Part2--
# New policy
