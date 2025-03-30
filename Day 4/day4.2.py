from collections import defaultdict

with open("input.txt","r") as file:
    lines = [line.strip() for line in file]

lines = [line[line.index(":") + 2:] for line in lines]
lines = [line.strip().split("|") for line in lines]
lines = [[line[0].split(), line[1].split()] for line in lines]

total = 0

cards = defaultdict(int)

for num in range(len(lines)):
    cards[num + 1] = 1

for line_num, line in enumerate(lines):
    matches = 0
    for num in line[0]:
        if num in line[1]:
            matches += 1
    for i in range(1, matches + 1):
        cards[line_num + i + 1] += cards[line_num + 1]

print(sum(cards.values()))
    
