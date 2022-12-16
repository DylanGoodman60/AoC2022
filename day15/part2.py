class Sensor():
    def __init__(self, x, y, bx, by):
        self.x = x
        self.y = y
        self.range = abs(x - bx) + abs(y - by)
        self.edge_points = set()

def in_range(p):
    if p[0] < 0 or p[0] > 4_000_000: return False
    if p[1] < 0 or p[1] > 4_000_000: return False
    return True

def find_point():
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

    # taxi around
    for s in sensors:
        for i in range(0, s.range+1):
            s.edge_points.add((s.x+i+1, s.y + s.range - i))
            s.edge_points.add((s.x+i+1, s.y - s.range + i))
            s.edge_points.add((s.x-i-1, s.y + s.range - i))
            s.edge_points.add((s.x-i-1, s.y - s.range + i))

    possible = []
    for i in sensors:
        for j in sensors:
            if i is j: break
            points = i.edge_points.intersection(j.edge_points)
            for p in points:
                if p not in beacons and in_range(p): 
                    possible.append(p)

    for p in possible:
        found = 1
        for s in sensors:
            if (abs(p[0] - s.x) + abs(p[1] - s.y)) <= s.range:
                found = 0
                break
        if found == 1: return p[0]*4000000 + p[1]
        found = 1
print(find_point())