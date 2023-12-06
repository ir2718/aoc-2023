from tqdm import tqdm

seeds = []
maps = [
    [],[],[],[],[],[],[]
]

with open("files/day-5.txt", "r") as f:
    lines = f.read()
lines = lines.split("\n\n")

for i, l in enumerate(lines[1:]):
    l = l.split("\n")[1:]

    for mapping in l:
        if mapping == "":
            continue
        parsed_mapping = tuple(list(map(int, mapping.split())))
        maps[i].append(parsed_mapping)

seed_nums = [int(x) for x in lines[0].split(":")[1].split() if x != ""]
seed_nums_grouped = sorted([
    (seed_nums[x], seed_nums[x] + seed_nums[x+1]) for x in range(0, len(seed_nums) - 1, 2)], 
    key=lambda x: (x[0], x[1])
)

solution_start = 50_000_000
while True:
    solution = solution_start
    for curr_map in maps[::-1]:
        for map_j in curr_map:
            if map_j[0] <= solution < map_j[0] + map_j[2]:
                solution = map_j[1] + solution - map_j[0]
                break
    

    for start, end in seed_nums_grouped:
        if start <= solution < end:
            print(f"Found solution: {solution_start, solution}")
            exit(0)

    solution_start += 1

    if solution_start % 10000  == 0:
        print(f"at: {solution_start}")