with open("day1_input.txt","r") as file:
    lines = [line for line in file]

total = 0

for line in lines:
    nums = [int(i) for i in line if i.isdigit()]
    num = int(str(nums[0]) + str(nums[-1]))
    print(num)
    total += num

print(total)