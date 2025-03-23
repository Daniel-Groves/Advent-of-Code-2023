with open("day2_input.txt","r") as file:
    lines = [line.strip() for line in file]

total = 0

for line in lines:
    b_max = 0
    r_max = 0
    g_max = 0
    line = (line.split(":")[1]).strip().split(";")
    line = [i.strip().split(",") for i in line]
    for game in line:
        for colour in game:
            num = colour.strip().split(" ")[0]
            if "red" in colour:
                r_max = max(r_max, int(num))
            if "green" in colour:
                g_max = max(g_max, int(num))
            if "blue" in colour:
                b_max = max(b_max, int(num))

    total += r_max * g_max * b_max

print(total)
