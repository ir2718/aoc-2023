import math

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

        cubes_in_game = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for t in turns:
            cube_set = t.split(",")
            
            for cubes in cube_set:
                num, color = cubes.strip().split(" ")
                cubes_in_game[color] = max(cubes_in_game[color], int(num))
        
        res += math.prod(cubes_in_game.values())
        
                
print(res)