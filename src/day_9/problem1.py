with open("files/day-9.txt", "r") as f:
    lines = [list(map(int, x.strip().split())) for x in f]


final_res = 0
for l in lines:
    curr_diffs = l
    all_diffs = [curr_diffs]
    while len(set(curr_diffs)) != 1:
        curr_diffs = [curr_diffs[i] - curr_diffs[i-1] for i in range(1, len(curr_diffs))]
        all_diffs.append(curr_diffs)


    res = 0
    for i in range(len(all_diffs)-1, -1, -1):
        res += all_diffs[i][-1]
    
    final_res += res
print(final_res)