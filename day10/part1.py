f = open("input.txt")
data = f.read().split("\n")

x = 1
cycle = 1
signals = [0]

for line in data:
    if 'noop' in line:
        signals.append(x)
        cycle += 1
    else:
        cmd, amount = line.rstrip().split(' ')
        signals.append(x)
        cycle += 1
        signals.append(x)
        x += int(amount)
        cycle += 1

targets = [20, 60, 100, 140, 180, 220]
total = sum([signals[i]*i for i in targets])
print(total)