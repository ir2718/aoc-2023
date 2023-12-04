with open("files/day-4.txt", "r") as f:
    res = 0
    for line in f:
        line = line[line.index(":") + 1:]
        split = line.split("|")

        s1, s2 = set(split[0].split()), set(split[1].split())
        intersection = s1.intersection(s2)

        if len(intersection) != 0:
            res += 2 ** (len(intersection) - 1)

print(res)