import math

time, distance = [], []

with open("files/day-6.txt", "r") as f:
    for line in f:
        if line.startswith("Time:"):
            time = [int(x) for x in line.split(":")[1].split(" ") if x != ""]
        elif line.startswith("Distance:"):
            distance = [int(x) for x in line.split(":")[1].split(" ") if x != ""]


res = []
for t_max, s_max in zip(time, distance):
    lower = math.floor(  (t_max - math.sqrt(t_max**2 - 4 * s_max )) / 2 ) + 1
    upper = math.ceil( (t_max + math.sqrt(t_max**2 - 4 * s_max )) / 2 ) - 1
    num_solutions = upper - lower + 1
    res.append(num_solutions)
res = math.prod(res)

print(res)