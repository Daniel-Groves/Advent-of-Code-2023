maps = []

lowest = float("inf")

with open("input.txt","r") as file:
    curr_map = []
    for line in file:
        if line.startswith("seeds"):
            seeds = [int(i) for i in line.strip().split(" ", 1)[1].split(" ")]
        elif line.endswith("map:\n"):
            if curr_map: maps.append(curr_map)
            curr_map = []
        elif line.strip():
            curr_map.append([int(i) for i in line.strip().split(" ")])
    if curr_map: maps.append(curr_map)

for seed in seeds:
    tracker = seed
    for map in maps:
        for mapping in map:
            if mapping[1] <= tracker <= mapping[1] + mapping[2]:
                tracker = mapping[0] + (tracker - mapping[1])
                break
    lowest = min(lowest, tracker)

print(lowest)