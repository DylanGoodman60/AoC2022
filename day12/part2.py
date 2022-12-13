f = open("input.txt")
data = [[ord(i)-96 for i in x] for x in f.read().split("\n")]

# locate start and end coordinates
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == -13:
            data[i][j] = 1
        if data[i][j] == -27:
            data[i][j] = 27
            r_s, c_s = i, j


# thanks to williamfiset on YT for a great visualization of BFS on 2d arrays
# https://www.youtube.com/watch?v=KiCBXu4P-2Y&t=547s&ab_channel=WilliamFiset

def BFS(data, r_s, c_s): 
    move_count = 0
    nodes_left_in_layer = 1
    nodes_in_next_layer = 0

    Q = [] 
    Q.append((r_s, c_s))
    visited = set((r_s, c_s))

    while( len(Q) > 0 ):
        r, c = Q.pop(0)
        if data[r][c] == 1:
            return move_count
        for i in [[-1, 0], [1,0], [0,1], [0,-1]]:
            rr = r + i[0]
            cc = c + i[1]
            if rr < 0 or cc < 0: continue
            if rr >= len(data) or cc >= len(data[0]): continue

            if (rr, cc) in visited: continue
            if (data[rr][cc] + 1 < (data[r][c])): continue
            Q.append((rr, cc))
            visited.add((rr, cc))
            nodes_in_next_layer += 1
        nodes_left_in_layer -= 1
        if nodes_left_in_layer == 0:
            move_count += 1
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
    return -1

print(BFS(data, r_s, c_s))