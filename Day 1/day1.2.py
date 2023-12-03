import time

with open("day1_input.txt","r") as file:
    lines = [line for line in file]
    

TOTAL = 0

word_to_number = {"one": 1,
                  "two": 2,
                  "three": 3,
                  "four": 4,
                  "five": 5,
                  "six": 6,
                  "seven": 7,
                  "eight": 8,
                  "nine": 9
                }


for line in lines:
    num = ""
    lengths = [3,4,5]
    for count in range(len(line)):
        if line[count].isdigit():
            num += line[count]
            break
        else:
            for length in lengths:
                converted = word_to_number.get(line[count:count+length])
                if converted:
                    num += str(converted)
                    break
            if converted:
                break
            
    for count in range(len(line)-1,-1,-1):
        if line[count].isdigit():
            num += line[count]
            break
        else:
            for length in lengths:
                try:
                    converted = word_to_number.get(line[count-length:count])
                except:
                    pass
                if converted:
                    num += str(converted)
                    break
            if converted:
                break
    if len(num) == 1:
        num += num
    
    TOTAL += int(num)
    print(num)

print(TOTAL)
