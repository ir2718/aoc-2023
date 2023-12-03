digits = {
    "one":"o1e", 
    "two":"t2o", 
    "three":"t3e", 
    "four":"f4r", 
    "five":"f5e", 
    "six":"s6x", 
    "seven":"s7n", 
    "eight":"e8t", 
    "nine":"n9e",
}

res = 0
with open("files/day-1.txt", "r") as f:
    for line in f:

        for k, v in digits.items():
            line = line.replace(k, v)

        chars = [c for c in line if c.isdigit()]
        res += int(chars[0] + chars[-1])

print(res)