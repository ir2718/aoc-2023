with open("files/day-4.txt", "r") as f:
    lines = f.readlines()

values = [1 for _ in range(len(lines))]
for l in lines:
    curr_num = int(l[l.index(" ")+1:l.index(":")].strip())

    line = l[l.index(":") + 1:]
    split = line.split("|")

    s1, s2 = set(split[0].split()), set(split[1].split())
    intersection = s1.intersection(s2)

    for i in range(values[curr_num - 1]):
        for k in range(len(intersection)):
            values[curr_num + k] += 1

res = sum(values)
print(res)