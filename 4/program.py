
def get_range(x):
    s, e = x.split('-')
    s, e = int(s), int(e)
    return list(range(s, e+1))

def has_full_overlap(pair):
    return all(x in pair[1] for x in pair[0]) or all(x in pair[0] for x in pair[1])

def has_overlap(pair):
    return any(x in pair[1] for x in pair[0]) or any(x in pair[0] for x in pair[1])

with open('input.txt') as f:
    content = f.read().split('\n')
    content = list(filter(lambda x: x != '', content))

    content = map(lambda x: x.split(','), content)
    content = map(lambda x: (get_range(x[0]), get_range(x[1])), content)
    content = list(content)

    full_overlaps = len(list(filter(lambda pair: has_full_overlap(pair), content)))
    overlaps = len(list(filter(lambda pair: has_overlap(pair), content)))

    print(full_overlaps)
    print(overlaps)

