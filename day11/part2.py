import math

class Monkey:
    def __init__(self, items, operation, test, pass_T, pass_F):
        self.items = items
        self.operation = operation
        self.test = test
        self.pass_T = pass_T
        self.pass_F = pass_F
        self.inspects = 0
    def __str__(self):
        return str(self.items) + str(self.operation) + " " + str(self.test) + " " + str(self.pass_T) + " " + str(self.pass_F)

f = open("input.txt")
monkey_data = [mon.split("\n") for mon in f.read().split("\n\n")]
monkeys = []
for mon in monkey_data:
    items = [int(i) for i in mon[1].split(':')[1].split(",")]
    operation = mon[2].split('old', 1)[1]
    test = int(mon[3].split('by', 1)[1])
    pass_t = int(mon[4].split('monkey')[1])
    pass_f = int(mon[5].split('monkey')[1])
    m = Monkey(items, operation, test, pass_t, pass_f)
    monkeys.append(m)

def calc_worry(num, oper):
    term = num
    if 'old' not in oper:
        term = int(oper.split(" ")[2])
    if '+' in oper:
        return num + term
    return num * term

lcm = math.lcm(*[m.test for m in monkeys])
rounds = 10_000
for r in range(rounds):
    for m in monkeys:
        for i in range(len(m.items)):
            m.inspects += 1
            item = m.items.pop(0)
            worry = calc_worry(item, m.operation)
            if (worry % m.test == 0):
                monkeys[m.pass_T].items.append(worry % lcm)
            else:
                monkeys[m.pass_F].items.append(worry % lcm)

arr = sorted([m.inspects for m in monkeys], reverse=True)
print(arr[0]*arr[1])
