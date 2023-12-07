
lines = []
with open("files/day-7.txt", "r") as f:
    for l in f:
        line = l.strip().split()
        line[1] = int(line[1])
        lines.append(line)


def get_higher_card(x, y):
    initial_ranking = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    for xi, yi in zip(x, y):
        first_idx, second_idx = initial_ranking.index(xi), initial_ranking.index(yi)
        if first_idx < second_idx:
            return False
        elif first_idx > second_idx:
            return True

def second_is_greater(x, y):
    # five of a kind
    if len(set(x)) == 1 and len(set(y)) == 1:
        return get_higher_card(x, y)
    elif len(set(x)) == 1:
        return False
    elif len(set(y)) == 1:
        return True

    x_d = sorted([x.count(xi) for xi in set(x)])
    y_d = sorted([y.count(yi) for yi in set(y)])
    
    # four of a kind
    if len(x_d) == 2 and x_d == [1, 4] and len(y_d) == 2 and y_d == [1, 4]:
        return get_higher_card(x, y)
    elif len(x_d) == 2 and x_d == [1, 4]:
        return False
    elif len(y_d) == 2 and y_d == [1, 4]:
        return True
    
    # full house
    if len(x_d) == 2 and x_d == [2, 3] and len(y_d) == 2 and y_d == [2, 3]:
        return get_higher_card(x, y)
    elif len(x_d) == 2 and x_d == [2, 3]:
        return False
    elif len(y_d) == 2 and y_d == [2, 3]:
        return True
    
    # three of a kind
    if len(x_d) == 3 and x_d == [1, 1, 3] and len(y_d) == 3 and y_d == [1, 1, 3]:
        return get_higher_card(x, y)
    elif len(x_d) == 3 and x_d == [1, 1, 3]:
        return False
    elif len(y_d) == 3 and y_d == [1, 1, 3]:
        return True
    
    # two pair
    if len(x_d) == 3 and x_d == [1, 2, 2] and len(y_d) == 3 and y_d == [1, 2, 2]:
        return get_higher_card(x, y)
    elif len(x_d) == 3 and x_d == [1, 2, 2]:
        return False
    elif len(y_d) == 3 and y_d == [1, 2, 2]:
        return True

    # one pair
    if len(x_d) == 4 and x_d == [1, 1, 1, 2] and len(y_d) == 4 and y_d == [1, 1, 1, 2]:
        return get_higher_card(x, y)
    elif len(x_d) == 4 and x_d == [1, 1, 1, 2]:
        return False
    elif len(y_d) == 4 and y_d == [1, 1, 1, 2]:
        return True
    
    # high card
    return get_higher_card(x, y)

for i, xi in enumerate(lines):
    max_idx = i
    for j in range(i+1, len(lines)):
        yj = lines[j]
        if second_is_greater(lines[max_idx][0], yj[0]):
            max_idx = j
    lines[i], lines[max_idx] = lines[max_idx], lines[i]

res = sum([x[1] * (i + 1) for i, x in enumerate(reversed(lines))])
print(res)