
def split_in_half(x):
    t = int(len(x)/2)
    return (x[:t], x[t:])

def get_value(x):
    if x.islower():
        return ord(x)-ord('a')+1
    return ord(x)-ord('A')+27

def group_rucksacks(c):
    groups = []
    for i in range(0, len(c), 3):
        groups.append([c[i], c[i+1], c[i+2]])
    return groups

with open('input.txt') as f:
    content = f.read().split('\n')
    content = list(filter(lambda x: x != '', content))

    groups = group_rucksacks(content)

    content = map(lambda x: split_in_half(x), content)
    content = map(lambda x: list(set(x[0]).intersection(x[1])), content)

    total = 0
    for rucksack in content:
        for item in rucksack:
            total += get_value(item)

    print(total)

    badge_total = 0
    for group in groups:
        badge = list(set(group[0]).intersection(group[1]).intersection(group[2]))
        badge_total += get_value(badge[0])

    print(badge_total)

