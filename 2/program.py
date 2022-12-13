
def parse(ch):
    if ch in ('A', 'X'): # rock
        return 1
    if ch in ('B', 'Y'): # paper
        return 2
    if ch in ('C', 'Z'): # scissors
        return 3

def evaluate(op, me):
    table = [
        [1, 1, 3], # rock 1 vs. rock 1 => draw
        [2, 1, 0], # paper 2 vs. rock 1 => loose
        [3, 1, 6], # scissors 3 vs. rock 1 => win

        [1, 2, 6], # rock 1 vs. paper 2 => win
        [2, 2, 3], # paper 2 vs. paper 2 => draw
        [3, 2, 0], # scissors 3 vs. paper 2 => loose

        [1, 3, 0], # rock 1 vs. scissors 3 => loose
        [2, 3, 6], # paper 2 vs. scissors 3 => win
        [3, 3, 3]  # scissors 3 vs. scissors 3 => draw
    ]

    result = filter(lambda x: x[0] == op and x[1] == me, table)
    return list(result)[0][2]

def evaluate_reverse(op, res):
    table = [
        [1, 1, 'Y'], # rock 1 vs. rock 1 => draw
        [2, 1, 'X'], # paper 2 vs. rock 1 => loose
        [3, 1, 'Z'], # scissors 3 vs. rock 1 => win

        [1, 2, 'Z'], # rock 1 vs. paper 2 => win
        [2, 2, 'Y'], # paper 2 vs. paper 2 => draw
        [3, 2, 'X'], # scissors 3 vs. paper 2 => loose

        [1, 3, 'X'], # rock 1 vs. scissors 3 => loose
        [2, 3, 'Z'], # paper 2 vs. scissors 3 => win
        [3, 3, 'Y']  # scissors 3 vs. scissors 3 => draw
    ]

    result = filter(lambda x: x[0] == op and x[2] == res, table)
    return list(result)[0][1]

def result_to_score(res):
    if res == 'Y': return 3
    if res == 'X': return 0
    if res == 'Z': return 6

def calculate_score(line):
    op, me = map(lambda x: parse(x), line.split(' '))

    score = me + evaluate(op, me)

    # print(f'op: {op} me: {me} = score: {score} ({me} + {evaluate(op, me)})')

    return score

def calculate_reverse_score(line):
    op, res = line.split(' ')
    op = parse(op)

    score = result_to_score(res) + evaluate_reverse(op, res)

    # print(f'op: {op} me: {me} = score: {score} ({me} + {evaluate(op, me)})')

    return score


with open('input.txt') as f:
    content = f.read().split('\n')

    # 1
    total = sum(map(lambda line: calculate_score(line), content))

    # 2
    total = sum(map(lambda line: calculate_reverse_score(line), content))

    print(total)


