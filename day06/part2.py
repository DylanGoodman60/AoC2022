f = open("input.txt")
data = f.read()

for i in range(len(data) - 14):
    mySet = {i for i in data[i:i+14]}
    if len(mySet) == 14: print(i+14)
        break
