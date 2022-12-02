f = open("input.txt")
line = f.read().replace(" ", "").replace("\n", '')
line_length = len(line)

rules = {0:3, 1:0, -2:0, -1:6, 2:6}

points = 0
for i in range(0, line_length, 2):
    them = ord(line[i])-64
    me = ord(line[i+1])-87
    points += me + rules[them - me]

print(points)