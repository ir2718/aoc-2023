with open("files/day-13.txt", "r") as f:
    lines = []
    curr_segment = []
    for line in f:
        if line == "\n":
            lines.append(curr_segment)
            curr_segment = []
        else:
            curr_segment.append(list(line.strip()))
    lines.append(curr_segment)

def check_vertical(segment, solution=None):
    for k in range(len(segment[0]) - 1):
        reflected = True
        z = 0

        while k-z >= 0 and k+z+1 <= len(segment[0]) - 1:
            col_l = [segment[i][k-z] for i in range(len(segment))]
            col_r = [segment[i][k+z+1] for i in range(len(segment))]
            if col_l != col_r:
                reflected = False
                break
            z += 1

        if reflected:
            if solution is None:
                return k + 1
            elif k + 1 != solution:
                return k + 1

    return 0

def check_horizontal(segment, solution=None):
    for k in range(len(segment) - 1):
        reflected = True
        z = 0

        while k-z >= 0 and k+z+1 <= len(segment) - 1:
            if segment[k-z] != segment[k+z+1]:
                reflected = False
                break
            z += 1

        if reflected:
            if solution is None:
                return k + 1
            elif k + 1 != solution:
                return k + 1

    return 0

res = 0
for segment in lines:
    cols = check_horizontal(segment)
    rows = check_vertical(segment)
    res += cols + rows * 100
print(res)