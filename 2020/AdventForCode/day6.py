import re

with open("C:\\Users\\Judith\\Documents\\AdventForCode\\day6_input.txt", "r") as file:
    input = file.readlines()

grouplst = []
entry = ""

end = 0
groupyes = []
for line in input:
    if  not re.match("^\n", line):
        end += 1
        if end == 1:
            yes_old = set(line.strip())
        else:
            yes_new = set(line.strip())
            yes_old = set(yes_new&yes_old)
    else:
        groupyes.append(len(yes_old))
        end = 0
if end != 0:
    groupyes.append(len(yes_old))

print(f"The sum of the question answered by everyone in the group for all groups is {sum(groupyes)}")

groupyes = []
for group in grouplst:
    letterlst = []
    for letter in group:
        if not letter in letterlst:
            letterlst.append(letter)
    groupyes.append(len(letterlst))

print(f"The sum of the questions asnwered with yes for all groups is {sum(groupyes)}.")