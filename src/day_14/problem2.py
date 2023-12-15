from copy import deepcopy
from tqdm import tqdm

with open("files/day-14.txt", "r") as f:
    lines = [list(x.strip()) for x in f]

def roll_north(lines):
    for j in range(len(lines[0])):
        curr_cube = -1
        i = 0
        while i < len(lines):
            if lines[i][j] == "#":
                while i < len(lines) and lines[i][j] == "#":
                    i += 1
                curr_cube = i
                i += 1
            
            if i < len(lines) and lines[i][j] == "O":
                curr_i = i
                while i > curr_cube and i > 0:    
                    if lines[i-1][j] != ".":
                        break  
                    tmp = lines[i-1][j]
                    lines[i-1][j] = lines[i][j]
                    lines[i][j] = tmp
                    i -= 1
                i = curr_i

            i += 1
    return lines

def roll_south(lines):
    for j in range(len(lines[0])):
        curr_cube = len(lines)
        i = len(lines) - 1
        while i >= 0:
            if lines[i][j] == "#":
                while i >= 0 and lines[i][j] == "#":
                    i -= 1
                curr_cube = i
                i -= 1
            
            if i >= 0 and lines[i][j] == "O":
                curr_i = i
                while i < curr_cube and i < len(lines) - 1:    
                    if lines[i+1][j] != ".":
                        break  
                    tmp = lines[i+1][j]
                    lines[i+1][j] = lines[i][j]
                    lines[i][j] = tmp
                    i += 1
                i = curr_i

            i -= 1
    return lines

def roll_west(lines):
    for i in range(len(lines)):
        curr_cube = -1
        j = 0
        while j < len(lines[0]):
            if lines[i][j] == "#":
                while j < len(lines[0]) and lines[i][j] == "#":
                    j += 1
                curr_cube = j
                j += 1
            
            if j < len(lines[0]) and lines[i][j] == "O":
                curr_j = j
                while j > curr_cube and j > 0:    
                    if lines[i][j-1] != ".":
                        break  
                    tmp = lines[i][j-1]
                    lines[i][j-1] = lines[i][j]
                    lines[i][j] = tmp
                    j -= 1
                j = curr_j

            j += 1
    return lines

def roll_east(lines):
    for i in range(len(lines)):
        curr_cube = len(lines[0])
        j = len(lines[0]) - 1
        while j >= 0:
            if lines[i][j] == "#":
                while j >= 0 and lines[i][j] == "#":
                    j -= 1
                curr_cube = j
                j -= 1
            
            if j >= 0 and lines[i][j] == "O":
                curr_j = j
                while j < curr_cube and j < len(lines[0]) - 1:    
                    if lines[i][j+1] != ".":
                        break  
                    tmp = lines[i][j+1]
                    lines[i][j+1] = lines[i][j]
                    lines[i][j] = tmp
                    j += 1
                j = curr_j

            j -= 1
    return lines

all_lines = [deepcopy(lines)]
j = 0

cycle_start = 81
cycle_length = 51
goal = 1000000000

for i in tqdm(range(cycle_start + (goal - cycle_start) % cycle_length)):
    lines = roll_north(lines)
    if any([lines == x for x in all_lines]):
        print("north")
        print([k for k in range(len(all_lines)) if all_lines[k] == lines])
        break
    else:
        all_lines.append(deepcopy(lines))
        j += 1

    lines = roll_west(lines)
    if any([lines == x for x in all_lines]):
        print("west")
        print([k for k in range(len(all_lines)) if all_lines[k] == lines])
        break
    else:
        all_lines.append(deepcopy(lines))
        j += 1

    lines = roll_south(lines)
    if any([lines == x for x in all_lines]):
        print("south")
        print([k for k in range(len(all_lines)) if all_lines[k] == lines])
        break
    else:
        all_lines.append(deepcopy(lines))
        j += 1

    lines = roll_east(lines)
    if any([lines == x for x in all_lines]):
        print("east")
        print([k for k in range(len(all_lines)) if all_lines[k] == lines])
        break
    else:
        all_lines.append(deepcopy(lines))
        j += 1

res = 0
for i in range(len(lines)):
    weight = len(lines) - i
    res += weight * lines[i].count("O")
print(res)