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

lines_rolled = roll_north(lines)

res = 0
for i in range(len(lines_rolled)):
    weight = len(lines_rolled) - i
    res += weight * lines_rolled[i].count("O")
print(res)