import math

f = open("input.txt")
data = f.read().split("\n")

x = 1
cycle = 1
num_cycles = 240

# we count from one out here
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

CRT = [' ' for _ in range(num_cycles)]

for c in range(1, num_cycles+1):
    pos = signals[c]
    pos += (math.floor((c-1)/40))*40
    if pos in [c-2, c-1, c]:
        CRT[c-1] = '▮'

for i in range(1, num_cycles+1):
    print(CRT[i-1], end="")
    if i % 40 == 0:
        print("")