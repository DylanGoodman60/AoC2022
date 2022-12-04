def getPriority(r1, r2, r3):
    for char in r1:
      if r2.count(char) > 0:
        if r3.count(char) > 0:
          if(ord(char) > 96):
              return ord(char)-96
          else:
              return ord(char)-38

f = open("input.txt")
data = f.read().split("\n")
total = 0
for i in range(0, len(data), 3):
    total += getPriority(data[i], data[i+1], data[i+2])

print(total)
