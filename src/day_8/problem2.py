import math
from functools import reduce

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


start_nodes = [i for i in maps.keys() if i.endswith("A")]
num_steps = []
for start in start_nodes:
    steps = 0
    found = False
    curr = start
    while True:
        for i in instructions:
            if curr.endswith("Z"):
                found = True
                break

            curr = maps[curr][i]
            steps += 1
        
        if found:
            break
    num_steps.append(steps)

def lcm(numbers):
    return reduce(lambda x, y: x * y // math.gcd(x, y), numbers, 1)

print(lcm(num_steps))