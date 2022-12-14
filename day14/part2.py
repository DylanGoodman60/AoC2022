def get_sand():
    f = open("input.txt")
    lines = [i.split(" -> ") for i in f.read().split("\n")]
    def get_pair(line, i):
        return [int(line[i].split(",")[0]),int(line[i].split(",")[1])]

    pairs = []
    for line in lines:
        for i in range(len(line)-1):
            pairs.append([get_pair(line, i), get_pair(line, i+1)])

    def get_range(left, right):
        return range(min(left, right), max(left, right)+1, 1)

    rocks = set()
    for pair in pairs: # fill rocks
        for i in get_range(pair[0][0], pair[1][0]): # col
            rocks.add((i,pair[0][1]))
        for i in get_range(pair[0][1], pair[1][1]): # row
            rocks.add((pair[0][0], i))

    lower = max([i[1] for i in rocks])
    # drop sand
    sand = set()
    step = 0
    while(True):
        x, y = 500, 0
        not_resting = True
        while(not_resting):
            if y == lower + 2:
                rocks.add((x, y))
                step -= 1
                not_resting = False
            if (x, y+1) not in rocks:
                y += 1
            elif (x-1, y+1) not in rocks:
                x -= 1
                y += 1
            elif (x+1, y+1) not in rocks:
                x += 1
                y += 1
            elif (x,y+1) in rocks and (x-1, y+1) in rocks and (x+1, y+1) in rocks:
                rocks.add((x, y))
                not_resting = False
        step += 1
        if x == 500 and y == 0: return step
print(get_sand())