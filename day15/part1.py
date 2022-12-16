class Sensor():
    def __init__(self, x, y, bx, by):
        self.x = x
        self.y = y
        self.range = abs(x - bx) + abs(y - by)

f = open("input.txt")
data = f.read().split("\n")
sensors = []
beacons = set()
junk = ['Sensor at x=', ', y=', ': closest beacon is at x=', ', y=']
for l in data:
    new = l.replace(junk[0], ' ').replace(junk[1], ' ').replace(junk[2], ' ').replace(junk[3], ' ')
    nums = [int(i) for i in new.split()]
    beacons.add((nums[2], nums[3]))
    sensors.append(Sensor(*nums))

left = min([s.x - s.range for s in sensors])
right = max([s.x + s.range for s in sensors])

sum = 0
row_pos = 2000000
for i in range(left, right):
    for s in sensors:
        if i == s.x and s.y == row_pos:
            break
        elif (i, row_pos) in beacons:
            break
        elif (abs(i - s.x) + abs(row_pos - s.y)) <= s.range:
            sum += 1
            break

print(sum)