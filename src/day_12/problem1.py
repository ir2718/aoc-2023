from itertools import combinations
import re

with open("files/day-12.txt", "r") as f:
    lines = f.read().splitlines()

def create_regex(nums):
    regex = r"^\.*"
    for i in range(len(nums)-1):
        regex += fr'#{{{str(nums[i])}}}\.+'
    regex += fr'#{{{str(nums[-1])}}}\.*$'
    return re.compile(regex)

def brute_force(pattern, nums, regex):
    combs = combinations(list(range(len(pattern))), len(nums) )
    num_valid = 0
    for c in combs:
        
        j = 0
        valid = True
        while j < len(c) - 1:
            if c[j+1] - c[j] <= nums[j]:
                valid = False
            j += 1
        
        if not valid:
            continue

        pattern2 = list(pattern)
        for n, idx in zip(nums, c):
            pattern2[idx : idx + n] = ["#"] * n
        
        valid = True
        for char2, char in zip(pattern2, pattern):
            if (char2 == "#" and char not in ["#", "?"]) or (char2 == "." and char not in [".", "?"]):
                valid = False
                break

        if not valid:
            continue

        pattern2 = "".join(pattern2).replace("?", ".")
        if regex.fullmatch(pattern2) and len(pattern2) == len(pattern):
            num_valid += 1

    return num_valid

res = 0
for row in lines:
    row_split = row.split()
    pattern = row_split[0] * 5
    nums = [int(x) for x in row_split[1].split(",") * 5]

    regex = create_regex(nums)

    num_valid = brute_force(pattern, nums, regex)
    res += num_valid
print(res)