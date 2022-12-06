f = open("input.txt")
data = f.read()

for i in range(len(data) - 4):
    mySet = {i for i in data[i:i+4]}
    if len(mySet) == 4: print(i+4)
        break
