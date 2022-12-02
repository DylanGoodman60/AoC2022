f = open("input.txt")
line = f.read().replace(" ", "").replace("\n", '')
line_length = len(line)

rules = {1: {3:2, 2:1, 1:3},
         2: {1:4, 2:5, 3:6},
         3: {3:7, 2:9, 1:8}}

points = 0
for i in range(0, line_length, 2):
    them = ord(line[i])-64
    me = ord(line[i+1])-87
    points += rules[me][them]

print(points)