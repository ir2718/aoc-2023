res = 0
with open("files/day-1.txt", "r") as f:
    for line in f:
        chars = [x for x in line if x.isdigit()]
        res += int(chars[0] + chars[-1])
print(res)