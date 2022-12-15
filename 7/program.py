
tree = {}
path = []

def command(line):
    global path

    cmd = line.split(' ')

    if cmd[1] == 'cd':
        if cmd[2] == '/':
            path = ['/']
        elif cmd[2] == '..':
            path.pop()
        else:
            path.append(cmd[2])

    if cmd[1] == 'ls':
        pass

def listing(line):
    ls = line.split(' ')
    if ls[0] == 'dir':
        pass
    else:
        update_keys(ls)

def update_keys(ls):
    global tree, path

    for i in range(0, len(path)):
        key = ''.join(path[:i+1])
        if key in tree:
            tree[key] += int(ls[0])
        else:
            tree[key] = int(ls[0])

def dir_to_delete():
    global tree

    space = 70000000
    update = 30000000

    min_remove = abs(space - update - tree['/'])

    candidates = dict(filter(lambda x: x[1] > min_remove, tree.items()))
    dir_to_rm = min(candidates.items(), key=lambda x: x[1])

    print(dir_to_rm[1])


with open('input.txt') as f:
    content = map(lambda x: x.strip(), f.readlines())

    for line in content:
        if line.startswith('$'):
            command(line)
        else:
            listing(line)

    total = 0
    for key in tree:
        if tree[key] < 100000:
            total += tree[key]

    print(total)

    dir_to_delete()

