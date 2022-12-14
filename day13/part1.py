def compare(left, right):
    for l, r in zip(left, right):
        l_is_int = isinstance(l, int)
        r_is_int = isinstance(r, int)

        if l_is_int and r_is_int: # both integers
            if l < r: return 1
            elif l > r: return -1
        elif not l_is_int and not r_is_int: # both lists
            if compare(l, r) != 0:
                return compare(l, r)
        elif l_is_int: # just l is int
            if compare([l], r) != 0:
                return compare([l], r)
        else: # just r is int
            if compare(l, [r]) != 0:
                return compare(l, [r])

    if len(right) > len(left):
        return 1
    elif len(right) < len(left):
        return -1
    return 0

f = open("input.txt")

# thanks internet, eval is crazy
new = [[eval(line) for line in lines.split("\n")] 
        for lines in f.read().split("\n\n")]

sum = 0
for i in range(len(new)):
    if compare(new[i][0], new[i][1]) == 1:
        sum += i+1
print(sum)