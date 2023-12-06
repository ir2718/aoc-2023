import math

with open("files/day-6.txt", "r") as f:
    for line in f:
        if line.startswith("Time:"):
            time = int("".join([x for x in line.split(":")[1].split(" ") if x != ""]))
        elif line.startswith("Distance:"):
            distance = int("".join([x for x in line.split(":")[1].split(" ") if x != ""]))

lower = math.floor( (time - math.sqrt(time**2 - 4 * distance )) / 2 ) + 1
upper = math.ceil( (time + math.sqrt(time**2 - 4 * distance )) / 2 ) - 1
num_solutions = upper - lower + 1
print(num_solutions)