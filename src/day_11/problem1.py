from itertools import combinations
import re

with open("files/day-11.txt", "r") as f:
    lines = [x.strip() for x in f]

def add_rows(lines):
    lines_expanded = lines[:]
    regex = re.compile(r"\.*$")
    i, j = 0, 0

    line_len = len(lines)
    while j < line_len: 
        if regex.fullmatch(lines[j]):
            lines_expanded.insert(i + j, lines[j])
            i += 1
        j += 1
    return lines_expanded

def add_columns(lines):
    lines_expanded = lines[:]
    regex = re.compile(r"\.*$")
    k, j = 0, 0

    line_len = len(lines_expanded[0])
    while j < line_len: 
        if regex.fullmatch("".join([x[j+k] for x in lines_expanded])):
            for i in range(len(lines_expanded)):
                tmp = list(lines_expanded[i])
                tmp.insert(j + k, ".")
                lines_expanded[i] = "".join(tmp)
            k += 1
        j += 1

    return lines_expanded

def get_coordinates(lines):
    coordinates = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "#":
                coordinates.append([i, j])
    return coordinates

lines = add_rows(lines)
lines = add_columns(lines)
coordinates = get_coordinates(lines)

def manhattan_dist(x1, x2):
    return sum(abs(a - b) for a, b in zip(x1, x2))

dists = 0
for x1, x2 in combinations(coordinates, 2):
    dists += manhattan_dist(x1, x2)
print(dists)