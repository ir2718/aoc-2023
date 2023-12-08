with open("files/day-8.txt", "r") as f:
    lines = f.readlines()

instructions = list(lines[0].strip())

maps = {}
for l in lines[2:]:
    split = l.strip().split("=")
    outer_key = split[0][:-1]
    
    l, r = split[1].strip().split(",")
    l = l[1:]
    r = r[1:-1]
    
    maps[outer_key] = {"L": l, "R": r}


print(maps)
num_steps = 0
curr = "AAA"
while curr != "ZZZ":
    for i in instructions:
        curr = maps[curr][i]
        num_steps += 1

print(num_steps)