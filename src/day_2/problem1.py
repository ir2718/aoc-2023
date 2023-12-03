max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

res = 0
with open("files/day-2.txt", "r") as f:
    for line in f:
        left, right = line.split(":")

        turns = right.split(";")
        valid_game = True
        for t in turns:
            cube_set = t.split(",")
            
            for cubes in cube_set:
                num, color = cubes.strip().split(" ")

                max_in_color = max_cubes[color]
                if int(num) > max_in_color:
                    valid_game = False

        if valid_game:
            id_ = int(left.split(" ")[-1])
            res += id_

print(res)