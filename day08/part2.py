f = open("input.txt")

data = f.read().split("\n")
forest = [[int(tree) for tree in trees] for trees in data]
score = [[[0,0,0,0] for _ in x] for x in data]

def rotate(arr):
    # cunning
    # [::-1] reverse elements in array
    # * unpacking operator
    # zip makes a tuple from each el in unpacked list
    # convert tuple back to list of ints before returning
    new = []
    for mat in arr:
        list_tuples = zip(*mat[::-1])
        new.append([list(el) for el in list_tuples])
    
    return new

def get_score(x, y):
    # if y == len(forest[0])-1:
    #     return 0

    points = 0
    for tree in forest[x][y+1::]:
        if tree >= forest[x][y]:
            points +=1
            return points
        points += 1
    return points

for flip in range(4): # RIGHT UP LEFT DOWN
    for i in range(len(forest)):
        for j in range(len(forest[0])):
            score[i][j][flip] = get_score(i, j)
    forest, score = rotate([forest, score])
forest, score = rotate([forest, score])

best = 0
temp = 1
for points in score:
    for point in points:
        for p in point:
            temp *= p
        best = max(temp, best)
        temp = 1
print(best)
