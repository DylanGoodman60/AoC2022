class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []
        self.size = 0

f = open("input.txt")
info, *data = f.read().split("\n")

root = Dir(info.split(" ")[2], 1)
temp = root
for cmd in data:
    if "dir" in cmd:
        temp.children.append(Dir(cmd.split(" ")[1], temp))
    elif "$" in cmd and "cd" in cmd and ".." not in cmd:
        for d in temp.children:
            if d.name == cmd.split(" ")[2]:
                temp = d
    elif "cd" in cmd and ".." in cmd:
        temp = temp.parent
    elif "$" not in cmd:
        temp.files.append(int(cmd.split(" ")[0]))


def give_sizes(node):
    total = 0
    for child in node.children:
        total += give_sizes(child)
    total += sum(node.files)
    node.size = total
    return total

def get_sizes(node):
    total = 0
    for child in node.children:
        total += get_sizes(child)
    
    if (node.size <= 100000):
        total += node.size
    return total

            
give_sizes(root)
print(get_sizes(root))