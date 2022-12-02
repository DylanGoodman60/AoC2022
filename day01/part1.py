f = open("input.txt")
most_calories = 0
sum_calorie = 0

for line in f.read().split("\n\n"):
    sum_calorie = 0
    for num in line.split("\n"):
        sum_calorie += int(num)
        most_calories = max(sum_calorie, most_calories)

print(most_calories)