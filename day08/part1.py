f = open("input.txt")

data = f.read().split("\n")
forest = [[int(tree) for tree in trees] for trees in data]
score = [[0 for _ in x] for x in data]

def scan():
    for i in range(0, len(forest), 1):
        max_hi = -1
        for j in range(0, len(forest[0]), 1):
            if forest[i][j] > max_hi:
                score[i][j] = 1
                max_hi = forest[i][j]

def rotate(arr):
    # cunning
    # [::-1] reverse elements in array
    # * unpacking operator
    # zip makes a tuple from each el in unpacked list
    # convert tuple back to list of ints before returning
    list_tuples = zip(*arr[::-1])
    return [list(el) for el in list_tuples]

for _ in ["RIGHT", "BOTTOM", "LEFT", "TOP"]:
    scan()
    forest = rotate(forest)
    score = rotate(score)

print(sum([sum(x) for x in score]))



