def find_sum_of_adjacent_numbers(line, indexes):
    i = 0
    res = 0
    while i < len(line):
        if i in indexes and line[i].isdigit():
            j = i
            curr_str = ""

            while line[j].isdigit():
                j -= 1
            j += 1

            while j < len(line) and line[j].isdigit():
                curr_str += line[j]
                j += 1
            
            i = j
            res += int(curr_str)
        else:
            i += 1
    return res

def find_symbol_indexes_for_line(line):
    symbol_indexes = set()
    for i, c in enumerate(line):
        if not c.isdigit() and c != ".":
            symbol_indexes.update([i-1, i, i+1])

    return symbol_indexes

with open("files/day-3.txt", "r") as f:
    l = [line.strip() for line in f]
l.append("."*len(l[0]))

symbol_indexes_prev, symbol_indexes_curr, symbol_indexes_next = None, None, None
final_res = 0
for i in range(len(l)-1):
    symbol_indexes = set()
    if symbol_indexes_prev is None:
        if i != 0:
            prev_line = l[i-1]
            symbol_indexes_prev = find_symbol_indexes_for_line(prev_line)
            symbol_indexes.update(symbol_indexes_prev)
    else:
        symbol_indexes_prev = symbol_indexes_curr
        symbol_indexes.update(symbol_indexes_prev)
    
    curr_line = l[i]
    if symbol_indexes_curr is None:
        symbol_indexes_curr = find_symbol_indexes_for_line(curr_line)
    else:
        symbol_indexes_curr = symbol_indexes_next
    symbol_indexes.update(symbol_indexes_curr)
    
    next_line = l[i+1]
    symbol_indexes_next = find_symbol_indexes_for_line(next_line)
    symbol_indexes.update(symbol_indexes_next)

    final_res += find_sum_of_adjacent_numbers(curr_line, symbol_indexes)
    i += 1
print(final_res)
