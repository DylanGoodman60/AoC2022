f = open("input.txt")

data = f.read().split("\n")

class Point:
    def __init__(self, xS, yS):
        self.x = xS
        self.y = yS

def move(p, dir):
    if dir == 'R':
        p.x += 1
    elif dir == 'L':
        p.x -= 1
    elif dir == 'U':
        p.y += 1
    elif dir == 'D':
        p.y -= 1


def follow(target, follow):
    xDist = target.x - follow.x
    yDist = target.y - follow.y
    if abs(xDist) == 2:
        if xDist > 0: follow.x += 1
        else: follow.x -= 1
        if (abs(yDist)) >= 1:
            if yDist > 0: follow.y += 1
            else: follow.y -= 1    
    if abs(yDist) == 2:
        if yDist > 0: follow.y += 1
        else: follow.y -= 1
        if (abs(xDist)) >= 1:
            if xDist > 0: follow.x += 1
            else: follow.x -= 1


H = Point(0,0)
T = Point(0,0)
visited = {(T.x, T.y)}

for line in data:
    dir, amount = line.rstrip().split(' ')
    for step in range(int(amount)):
        move(H, dir)
        follow(H, T)
        visited.add((T.x, T.y))
print(len(visited))