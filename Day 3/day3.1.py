import re

with open("input.txt","r") as file:
    lines = [line.strip() for line in file]

total = 0

for index, line in enumerate(lines):
    non_symbol = "1234567890."
    for match in re.finditer(r'\d+', line):
        num = match.group()
        num_index = match.start()
        adj = False
        start = -1 if num_index > 0 else 0
        end = 1 if num_index + len(num) < len(line) - 1 else 0
        for i in range(start, len(num) + end):
            if index > 0:
                if lines[index - 1][num_index + i] not in non_symbol:
                    adj = True
            if index < len(lines) - 1:
                if lines[index + 1][num_index + i] not in non_symbol:
                    adj = True
        if num_index > 0:
            if line[num_index - 1] not in non_symbol:
                adj = True
        if num_index + len(num) < len(line) - 1:
            if line[num_index + len(num)] not in non_symbol:
                adj = True

        if adj: 
            total += int(num)
            
print(total)