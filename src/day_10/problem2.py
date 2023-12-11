with open("files/day-10.txt", "r") as f:
    l = [list(x.strip()) for x in f]

def find_direction(prev_coord, curr_coord, l):
    char = l[curr_coord[0]][curr_coord[1]]

    if char == "|":
        if curr_coord[0] > prev_coord[0]:
            return [curr_coord[0] + 1, curr_coord[1]]
        return [curr_coord[0] - 1 , curr_coord[1]]
    
    elif char == "-":
        if curr_coord[1] > prev_coord[1]:
            return [curr_coord[0], curr_coord[1] + 1]
        return [curr_coord[0], curr_coord[1] - 1]
    
    elif char == "L":
        if curr_coord[0] > prev_coord[0]:
            return [curr_coord[0], curr_coord[1] + 1]
        return [curr_coord[0] - 1, curr_coord[1]]

    elif char == "J":
        if curr_coord[0] > prev_coord[0]:
            return [curr_coord[0], curr_coord[1] - 1]
        return [curr_coord[0] - 1, curr_coord[1]]

    elif char == "7":
        if curr_coord[0] < prev_coord[0]:
            return [curr_coord[0], curr_coord[1] - 1]
        return [curr_coord[0] + 1, curr_coord[1]]

    elif char == "F":
        if curr_coord[0] < prev_coord[0]:
            return [curr_coord[0], curr_coord[1] + 1]
        return [curr_coord[0] + 1, curr_coord[1]]

coords = set()
start_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
coord_dir_dist = []
for i in range(len(l)):
    for j in range(len(l[i])):
        for di, dj in start_directions:
            if l[i][j] == "S" and 0 <= i + di < len(l) and 0 <= j + dj < len(l[i]):
                coords.add((i, j))
                
                char = l[i + di][j + dj]
                if (di == -1 and dj == 0 and char in "|F7") or \
                    (di == 1 and dj == 0 and char in "|JL") or \
                    (di == 0 and dj == -1 and char in "-FL") or \
                    (di == 0 and dj == 1 and char in "-J7"):
                    coord_dir_dist.append([[i, j], [i + di, j + dj], 1])
                    coords.add((i+di, j+dj))

while coord_dir_dist[0][1] != coord_dir_dist[1][1]:
    for i in range(len(coord_dir_dist)):
        prev_prev_coord, prev_coord, cost = coord_dir_dist[i]
        next_coord = find_direction(prev_prev_coord, prev_coord, l)
        coords.add((next_coord[0], next_coord[1]))
        coord_dir_dist[i] = [prev_coord, next_coord, cost + 1]

coords = sorted(coords, key=lambda x: (x[0], x[1])) 
coords_per_row = []
for x in set(c[0] for c in coords):
    curr_elems = [c for c in coords if c[0] == x]
    coords_per_row.append(curr_elems)

l[96][101] = "L" 
num_tiles = 0
for i in range(len(l)):
    inside = False
    for j in range(len(l[i])):
        if (i, j) in coords and l[i][j] in "JL|":
            inside = not inside
        elif (i, j) not in coords and inside:
            num_tiles += 1 

print(num_tiles)