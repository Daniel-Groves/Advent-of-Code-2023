with open("day2_input.txt","r") as file:
    lines = [line.strip() for line in file]

comparison = [12,13,14]

TOTAL = 0

for line in lines:
    id = (line.split(":", 1)[0])[5:]
    line = (line.split(":", 1)[1])
    line = line.replace(" ", "")
    newline = line.split(";")
    newline = [i.split(",") for i in newline]
    #print(newline)
    for draw in newline:
        colours = [0,0,0]
        for colour in draw:
            if "red" in colour:
                colours[0] = int(colour[:-3])
            if "green" in colour:
                colours[1] = int(colour[:-5])
            if "blue" in colour:
                colours[2] = int(colour[:-4])
        if colours[0] > comparison[0] or colours[1] > comparison[1] or colours[2] > comparison[2]:
            possible = False
            break
        else:
            possible = True
    if possible:
        print(id)
        TOTAL += int(id)


print(TOTAL)
