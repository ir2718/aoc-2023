from copy import deepcopy
from tqdm import tqdm

with open("files/day-16.txt", "r") as f:
    lines = f.read().splitlines()

points = []
x = list(range(len(lines[0])))
y = list(range(len(lines)))
for yi in y:
    points.append([0, yi])
    points.append([len(lines[0]) - 1, yi])

for i in range(1, len(x)-1):
    points.append([x[i], 0])
    points.append([x[i], len(lines) - 1])

results = []
for p in tqdm(points):
    i, j = p
    
    start = []
    if j == 0:
        start.append([0, -1])
    elif j == len(lines[0]) - 1:
        start.append([0, 1])
    
    if i == 0:
        start.append([-1, 0])
    elif i == len(lines) - 1:
        start.append([1, 0])

    for v in start:
        curr, prev = [], None
        splits, directions = [], []
        beams = None

        while beams != []:
            if prev is None:
                i, j = p

                curr.append((i + v[0], j + v[1]))
                curr.append((i, j))

                beams = [[curr[-2], curr[-1]]]

            new_beams = []
            for k in range(len(beams)):
                prev_step, step = beams[k]
                to_append = []

                curr_char = lines[step[0]][step[1]] 

                if curr_char == "|":
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

                elif curr_char == "-":
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

                elif curr_char == "/":
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
                    
                elif curr_char == "\\":
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

                elif curr_char == ".":
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

            beams = new_beams
            prev = curr
            curr.extend([tuple(x[1]) for x in new_beams])

            
        results.append(len(set(curr)) - 1)

print(max(results))