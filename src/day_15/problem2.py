with open("files/day-15.txt", "r") as f:
    line = f.read().strip()

def hash_algo(str):
    hash_value = 0
    mul_const, div_const = 17, 256
    for ch in str:
        ascii = ord(ch)
        hash_value += ascii
        hash_value = hash_value * mul_const % div_const
    return hash_value

hashmap = [[] for _ in range(256)]

res = 0
for str in line.split(","):
    op = "=" if "=" in str else "-"
    split = str.split(op)
    start_str = split[0]

    hash_value = hash_algo(start_str)
    
    idx = [i for i, x in enumerate(hashmap[hash_value]) if x[0] == start_str]
    if op == "=":
        value = int(split[1])
        if len(idx) > 0:
            hashmap[hash_value][idx[0]][1] = value
        else:
            hashmap[hash_value].append([start_str, value])
    else:
        if len(idx) > 0:
            del hashmap[hash_value][idx[0]]
    
def calculate_focusing_power(hashmap):
    focusing_power = 0
    for i in range(len(hashmap)):
        for j in range(len(hashmap[i])):
            focusing_power += (i + 1) * (j + 1)* hashmap[i][j][1]
    return focusing_power

print(calculate_focusing_power(hashmap))
