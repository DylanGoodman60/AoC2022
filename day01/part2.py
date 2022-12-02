f = open("input.txt")
elves = []
sum_calorie = 0

for line in f.read().split("\n\n"):
    for num in line.split("\n"):
        sum_calorie += int(num)
    elves.append(sum_calorie)
    sum_calorie = 0

print(sum(sorted(elves)[-3:]))