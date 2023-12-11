from itertools import combinations
import re

with open("files/day-11.txt", "r") as f:
    lines = [x.strip() for x in f]

def idx_of_same(lines):
    regex = re.compile(r"\.*$")
    
    same_rows, same_cols = [], []
    for i in range(len(lines)):
        if regex.fullmatch(lines[i]):
            same_rows.append(i)

    for i in range(len(lines[0])):
        if regex.fullmatch("".join([x[i] for x in lines])):
            same_cols.append(i)

    return same_rows, same_cols

def get_coordinates(lines):
    coordinates = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "#":
                coordinates.append([i, j])
    return coordinates


def manhattan_dist(x1, x2):
    return sum(abs(a - b) for a, b in zip(x1, x2))

def expanded_dim_dist(x1_comp, x2_comp, same):
    return len([x for x in same if min(x1_comp, x2_comp) < x < max(x1_comp, x2_comp)])


to_expand = 1_000_000
same_rows, same_cols = idx_of_same(lines)
coordinates = get_coordinates(lines)

dists = 0
for x1, x2 in combinations(coordinates, 2):
    manhattan = manhattan_dist(x1, x2)
    row_dist = (to_expand - 1) * expanded_dim_dist(x1[0], x2[0], same_rows)
    col_dist = (to_expand - 1) * expanded_dim_dist(x1[1], x2[1], same_cols)
    dists += manhattan + row_dist + col_dist
print(dists)