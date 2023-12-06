seeds = []
maps = [
    [],[],[],[],[],[],[]
]

with open("files/day-5.txt", "r") as f:
    lines = f.read()
lines = lines.split("\n\n")

seeds = [int(x) for x in lines[0].split(":")[1].split() if x != ""]

for i, l in enumerate(lines[1:]):
    l = l.split("\n")[1:]

    for mapping in l:
        if mapping == "":
            continue
        parsed_mapping = tuple(list(map(int, mapping.split())))
        maps[i].append(parsed_mapping)


curr_values = seeds[:]
for curr_map in maps:
    for i in range(len(curr_values)):
        for map_j in curr_map:
            if map_j[1] <= curr_values[i] < map_j[1] + map_j[2]:
                curr_values[i] = map_j[0] + curr_values[i] - map_j[1]
                break

final_locs = sorted(curr_values, reverse=False)
print(final_locs)