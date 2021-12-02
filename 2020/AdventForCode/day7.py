
with open("C:\\Users\\Judith\\Documents\\AdventForCode\\day7_input.txt", "r") as file:
    input = file.readlines()

colorlst = []
linelst = []
skip = ["bags", "bag", "contain", ",", "."]
rules = dict()
for line in input:
    line = line.strip()
    for trash in skip:
        line = line.replace(trash, "")
    words = line.split(" ") # list of words per line
    words = list(filter(None, words))
    linelst.append(words) # add line-list to big list containing all lines
    color = " ".join(words[0:2])
    colorlst.append(color) # add color of line to color-list
    rules[color] = []
    for i in range(2, len(words) - 2, 3):
        rules[color].append((" ".join(words[i+1:i+3]),words[i]))

valid_colors = []
valid_colors_new = ["shiny gold"]
i = 0
while len(valid_colors) != len(list(set(valid_colors_new))):
    valid_colors = list(set(valid_colors_new[:]))
    for color in colorlst:
        for inside_color, nr in rules[color]:
            if (inside_color in valid_colors) and (color not in valid_colors):
                valid_colors_new.append(color)

print(f"Amount of luggage colors that can contain a shiny gold bag: {len(valid_colors) - 1}")

#---Part2---
def bags_inside(color):
    global nr_bags
    if rules[color]:
        for inside_color, nr in rules[color]:
            nr_bags += (1 + bags_inside(inside_color)) * int(nr)
            return nr_bags
                      
    else:
        return 0  
    return nr_bags       

nr_bags = 0                  
print(bags_inside("shiny gold"))