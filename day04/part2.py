f = open("input.txt")

total = 0
for line in f.read().split("\n"):
    p1, p2 = line.split(",")
    e1, e2 = p1.split("-"), p2.split("-")

    if int(e1[0]) >= int(e2[0]) and int(e1[0]) <= int(e2[1]):
        total += 1
    elif int(e1[1]) >= int(e2[0]) and int(e1[1]) <= int(e2[1]):
        total += 1
    elif int(e2[1]) >= int(e1[0]) and int(e2[1]) <= int(e1[1]):
        total += 1
    elif int(e2[0]) >= int(e1[0]) and int(e2[0]) <= int(e1[1]):
        total += 1

print(total)