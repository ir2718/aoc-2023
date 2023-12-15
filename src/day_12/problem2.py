with open("files/day-12-ex.txt", "r") as f:
    lines = f.read().splitlines()

def base_case(substr):
    pass

def recursion(pattern, nums, num_valid, i=0, memo={}):
    while set(pattern[i:i+nums[0]]) != {"#", "?"}:
        i += 1

    j = i+nums[0]
    while j < len(pattern) and pattern[j] != ".":
        j += 1
    
    return base_case * recursion(pattern[j])

res = 0
num_repeats = 5
for row in lines:
    row_split = row.split()
    pattern = row_split[0] * num_repeats
    nums = [int(x) for x in row_split[1].split(",") * num_repeats]

    num_valid = 0
    recursion(pattern, nums, num_valid)
    print(pattern, nums)