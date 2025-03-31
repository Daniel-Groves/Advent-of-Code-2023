maps = []

lowest = float("inf")

with open("input.txt","r") as file:
    curr_map = []
    for line in file:
        if line.startswith("seeds"):
            seeds = list(map(int, line.strip().split(" ", 1)[1].split(" ")))
        elif line.endswith("map:\n"):
            if curr_map: maps.append(curr_map)
            curr_map = []
        elif line.strip():
            curr_map.append([int(i) for i in line.split()])
    if curr_map: maps.append(curr_map)

for seed in seeds:
    tracker = seed
    for map in maps:
        for dest, src, length in map:
            if src <= tracker <= src + length:
                tracker = dest + (tracker - src)
                break
    lowest = min(lowest, tracker)

print(lowest)