import re
from collections import defaultdict
import math

with open("input.txt","r") as file:
    lines = [line.strip() for line in file]

total = 0

adjacent_directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0), (1, 1)]

gears = defaultdict(list)

for row, line in enumerate(lines):
    non_symbol = "1234567890."
    for match in re.finditer(r'\d+', line):
        num = match.group()
        col = match.start()
        length = len(num)
        adj = False
        gears_found = []

        for i in range(length):
            for dr, dc in adjacent_directions:
                r, c = row + dr, col + i + dc
                if 0 <= r < len(lines) and 0 <= c < len(lines[r]):
                    if lines[r][c] not in non_symbol:
                        if lines[r][c] == "*" and [r,c] not in gears_found:
                            gears[(r,c)].append(int(num))
                            gears_found.append([r, c])


for gear in gears:
    print(gears[gear])
    if len(gears[gear]) >= 2:
        total += math.prod(gears[gear])

            
print(total)