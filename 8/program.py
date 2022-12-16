
def is_edge(content, x, y):
    if x == 0 or x == len(content)-1:
        return True
    if y == 0 or y == len(content[0]) - 1:
        return True
    return False

def transpose(l):
    return list(map(list, zip(*l)))

def search_for_visible(content, transposed):
    visible = set()

    for x in range(0, len(content)):
        lm = 0
        rm = 0

        for y in range(0, len(content[x])):
            xt = x if not transposed else y
            yt = y if not transposed else x

            if is_edge(content, x, y):
                visible.add((xt, yt))
                lm = content[x][y]

            elif content[x][y] > lm:
                visible.add((xt, yt))
                lm = content[x][y]

                add_distance(xt, yt, y)
                if xt == 3 and yt == 2:
                    print(f'L: not-checking ({xt}, {yt}) => {y}')
            else:
                dist = 1
                if xt == 3 and yt == 2:
                    print(f'L: considering range: {0}, {y}')
                for z in range(0, y):
                    if content[x][y-z-1] < content[x][y]:
                        dist += 1
                    else:
                        break
                add_distance(xt, yt, dist)
                if xt == 3 and yt == 2:
                    print(f'checking ({xt}, {yt}) => {dist}')

            y_idx = len(content[x])-y-1

            xt = x if not transposed else y_idx
            yt = y_idx if not transposed else x

            if is_edge(content, x, y_idx):
                visible.add((xt, yt))
                rm = content[x][y_idx]

            elif content[x][y_idx] > rm:
                visible.add((xt, yt))
                rm = content[x][y_idx]

                add_distance(xt, yt, y)
                if xt == 3 and yt == 2:
                    print(f'R: not-checking ({xt}, {yt}) => {y}')
            else:
                dist = 1
                if xt == 3 and yt == 2:
                    print(f'R: considering range: {y_idx+1}, {len(content[x])}')
                for z in range(y_idx+1, len(content[x])):
                    if content[x][z] < content[x][y]:
                        dist += 1
                    else:
                        break
                add_distance(xt, yt, dist)
                if xt == 3 and yt == 2:
                    print(f'checking ({xt}, {yt}) => {dist}')

    return visible

def add_distance(x, y, distance):
    global trees

    key = (x, y)

    if key in trees:
        trees[key].append(distance)
    else:
        trees[key] = [distance]

def multiply(l):
    total = 1
    for x in l:
        total *= x
    return total

trees = {}

with open('input.txt') as f:
    content = map(lambda x: map(int, list(x.strip())), f.readlines())
    content = map(list, content)
    content = list(content)

    # 1
    visible = search_for_visible(content, transposed=False)
    content = transpose(content)
    visible = visible.union(search_for_visible(content, transposed=True))

    print(len(visible))

    # 2
    totals = list(map(lambda x: multiply(x[1]), trees.items()))

    print(max(totals))

