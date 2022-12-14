from functools import cmp_to_key

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
data = [eval(line) for line in f.read().replace("\n\n", "\n").split("\n")]
data.append([[2]])
data.append([[6]])

sort = sorted(data, key=cmp_to_key(compare), reverse=True)
print((sort.index([[2]])+1) * (sort.index([[6]])+1))
