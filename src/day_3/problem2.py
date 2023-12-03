with open("files/day-3.txt", "r") as f:
    l = [line.strip() for line in f]

tmp =  ["."*len(l[0])]
l = tmp + l + tmp

def find_number_in_line(line, idx):
    nums = []

    i = max(0, idx-1)
    while i < min(len(line), idx + 2):
        if line[i].isdigit():
            j = i
            while line[j].isdigit():
                j -= 1
            j += 1

            curr_str = ""
            while j < len(line) and line[j].isdigit():
                curr_str += line[j]
                j += 1

            nums.append(int(curr_str))

            i = j
        else:
            i += 1
    return nums

final_res = 0
for k in range(1, len(l)-1):
    for z, c in enumerate(l[k]):
        if not c.isdigit() and c != ".":
            prev_num = find_number_in_line(l[k-1], z)
            curr_num = find_number_in_line(l[k], z)
            next_num = find_number_in_line(l[k+1], z)

            all_nums = prev_num + curr_num + next_num
            if len(all_nums) == 2:
                final_res += all_nums[0] * all_nums[1]
print(final_res)