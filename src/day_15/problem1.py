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

res = 0
for str in line.split(","):
    res += hash_algo(str)
print(res)