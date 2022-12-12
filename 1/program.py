
with open('input.txt') as f:
    contnet = f.read()

    elves = contnet.split('\n\n')
    elves = map(lambda x: x.split('\n'), elves)
    elves = map(lambda x: filter(lambda y: y != '', x), elves)
    elves = map(lambda x: list(map(lambda y: int(y), x)), elves)
    elves = map(lambda x: sum(x), elves)
    elves = list(elves)

    # 1
    print(max(elves))

    # 2
    elves.sort(reverse=True)

    print(sum(elves[:3]))

