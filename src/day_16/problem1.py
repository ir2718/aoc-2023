from copy import deepcopy

with open("files/day-16.txt", "r") as f:
    lines = f.read().splitlines()

curr, prev = [], None
splits, directions = [], []
beams = None

while beams != []:
    if prev is None:
        i, j = 0, -1
        curr.append((i, j))
        curr.append((i, j + 1))

        beams = [[curr[-2], curr[-1]]]

    new_beams = []
    for k in range(len(beams)):
        prev_step, step = beams[k]
        to_append = []

        if lines[step[0]][step[1]] == "|":
            # from the side
            if prev_step[0] == step[0]:
                if step[0] - 1 >= 0:
                    to_append.append([step[0] - 1, step[1]])
                if step[0] + 1 < len(lines):
                    to_append.append([step[0] + 1, step[1]])
                splits.append(step)
                directions.append([step[0]-prev_step[0], step[1]-prev_step[1]] in [[0, -1], [0, 1]])
            # from bottom
            elif prev_step[0] - 1 == step[0] and step[0] - 1 >= 0:
                to_append.append([step[0] - 1, step[1]])
            # from top
            elif prev_step[0] + 1 == step[0] and step[0] + 1 < len(lines):
                to_append.append([step[0] + 1, step[1]])

        elif lines[step[0]][step[1]] == "-":
            if prev_step[1] == step[1]:
                # from up or down
                if step[1] + 1 < len(lines[0]):
                    to_append.append([step[0], step[1] + 1])
                if step[1] - 1 >= 0:
                    to_append.append([step[0], step[1] - 1])
                splits.append(step)
                directions.append([step[0]-prev_step[0], step[1]-prev_step[1]] in [[-1, 0], [1, 0]])
            elif prev_step[1] + 1 == step[1] and step[0] + 1 < len(lines):
                to_append.append([step[0], step[1] + 1])
            elif prev_step[1] - 1 == step[1] and step[1] - 1 >= 0:
                to_append.append([step[0], step[1] - 1])

        elif lines[step[0]][step[1]] == "/":
            # from the left
            if step[1] == prev_step[1] + 1 and step[0] - 1 >= 0: 
                to_append.append([step[0]-1, step[1]])
            # from the right
            elif step[1] == prev_step[1] - 1 and step[0] + 1 < len(lines):
                to_append.append([step[0] + 1, step[1]])
            # from up
            elif step[0] == prev_step[0] + 1 and step[1] - 1 >= 0:
                to_append.append([step[0], step[1] - 1])
            # from bottom
            elif step[0] == prev_step[0] - 1 and step[1] + 1 < len(lines[0]):
                to_append.append([step[0], step[1] + 1])
            
        elif  lines[step[0]][step[1]] == "\\":
            # from the left
            if step[1] == prev_step[1] + 1 and step[0] + 1 < len(lines):
                to_append.append([step[0] + 1, step[1]])
            # from the right
            elif step[1] == prev_step[1] - 1 and step[0] - 1 >= 0: 
                to_append.append([step[0] - 1, step[1]])
            # from up
            elif step[0] == prev_step[0] + 1 and step[1] + 1 < len(lines[0]):
                to_append.append([step[0], step[1] + 1])
            # from bottom
            elif step[0] == prev_step[0] - 1 and step[1] - 1 >= 0:
                to_append.append([step[0], step[1] - 1])

        elif lines[step[0]][step[1]] == ".":
            # from the left
            if step[1] == prev_step[1] + 1 and step[1] + 1 < len(lines[0]):
                to_append.append([step[0], step[1] + 1])
            # from the right
            elif step[1] == prev_step[1] - 1 and step[1] - 1 >= 0:
                to_append.append([step[0], step[1] - 1])
            # from bottom
            elif step[0] == prev_step[0] - 1 and step[0] - 1 >= 0:
                to_append.append([step[0] - 1, step[1]])
            # from up
            elif step[0] == prev_step[0] + 1 and step[0] + 1 < len(lines):
                to_append.append([step[0] + 1, step[1]])

        for x in to_append:
            idx = [i for i in range(len(splits)) if splits[i] == x]
            if idx == []:
               new_beams.append([step, x])
            else:
                if not directions[idx[0]]:
                    new_beams.append([step, x])

    beams = deepcopy(new_beams)
    prev = deepcopy(curr)
    curr.extend([tuple(x[1]) for x in new_beams])

print(len(set(curr))-1)
new_lines = []
lines = [list(l) for l in lines]
for i in range(len(lines)):
    tmp = []
    for j in range(len(lines[i])):
        if (i, j) in curr:            
            tmp.append("#")
        else:
            tmp.append(".")
    new_lines.append(tmp)

for x in new_lines:
    print("".join(x))
