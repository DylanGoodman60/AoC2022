def getPriority(ruck_str):
    half_len = int(len(ruck_str)/2)
    part1 = ruck_str[:half_len]
    part2 = ruck_str[half_len:]
    for char in part1:
        if part2.count(char) > 0:
            if(ord(char) > 96):
                return ord(char)-96
            else:
                return ord(char)-38

f = open("input.txt")
data = f.read().split("\n")
total = 0
for ruck in data:
    total += getPriority(ruck)

print(total)
