with open("input.txt","r") as file:
    lines = [line.strip() for line in file]

lines = [line[line.index(":") + 2:] for line in lines]
lines = [line.strip().split("|") for line in lines]
lines = [[line[0].split()] + [line[1].split()] for line in lines]

total = 0

for line in lines:
    points = 0
    for num in line[0]:
        if num in line[1]:
            if not points: points = 1
            else: points *= 2
    total += points

    
print(total)
    
