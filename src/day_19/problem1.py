with open("files/day-19.txt", "r") as f:
    rules, flows = f.read().split("\n\n")
    rules = rules.split()

    operator_dict = {
        ">": lambda x, y: x > y,
        "<": lambda x, y : x < y 
    }
    rule_dict = {}
    other_dict = {}
    for k in rules:
        name = k.split("{")[0]
        tmp = []
        for elem in k[:-1].split("{")[1].split(","):
            # if contains operator
            if len(elem) >= 2 and elem[1] in list(operator_dict.keys()):
                elem, next_ = elem.split(":")
                tmp.append(
                    (
                        elem[0],
                        elem[1],
                        int(elem[2:]),
                        next_
                    )
                )
            else:
                other_dict[name] = elem 
        rule_dict[name] = tmp

    flows = [{x[0]: int(x[2:]) for x in f[1:-1].split(",")} for f in flows.split()]

res = 0
for f in flows:
    curr_name = "in"
    while curr_name not in ["A", "R"]:
        rules = rule_dict[curr_name]
        
        found = False
        for a, op, b, next_ in rules:
            if operator_dict[op](f[a], b):
                curr_name = next_
                found = True
                break

        if not found:
            curr_name = other_dict[curr_name]

    if curr_name == "A":
        res += sum(f.values())

print(res)