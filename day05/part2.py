f = open("input.txt")
data = f.read()


def get_col(theData):
    for line in theData:
        if '1' in line:
            return int(line[len(line)-2])

def get_row_chars(line, bigArr):
    j = 0
    for i in range(1, len(line), 4):
        if line[i].isupper():
            bigArr[j].insert(0, line[i])
        j += 1

# parse stacks
info = [[] for i in range(get_col(data.split("\n")))]
for line in data.split("\n"):
    if '1' in line: break
    get_row_chars(line, info)

# parse instructions
rules = []
index = [5, 12, 17]
for line in data.split("\n"):
    if 'move' in line:
        rules.append([int(s) for s in line.split() if s.isdigit()])

for rule in rules:
    for block in range(rule[0]):
        pop_index = (len(info[rule[1]-1])) - (rule[0]-1) - 1 + block
        crate = info[rule[1]-1].pop(pop_index)
        info[rule[2]-1].append(crate)


arr = [crates.pop() for crates in info]
for num in arr:
    print(num, end="")
print("\n")