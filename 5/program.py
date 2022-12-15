
def parse_stacks(stacks):
    stacks = stacks.split('\n')

    stack_cols = stacks[-1]

    stacks = stacks[:-1]
    stacks.reverse()

    col_idxs = []
    cols = {}
    for i in range(0, len(stack_cols)):
        if stack_cols[i].isnumeric():
            col_idxs.append(i)
            cols[i] = []

    for row in stacks:
        for col in col_idxs:
            if len(row) < col: continue
            if row[col] == ' ': continue

            cols[col].append(row[col])

    return cols

with open('input.txt') as f:
    content = f.read()

    stacks, instructions  = content.split('\n\n')
    instructions = instructions.split('\n')
    instructions = filter(lambda x: x != '', instructions)

    cols = parse_stacks(stacks)
    cols2 = parse_stacks(stacks)

    col_idxs = list(cols.keys())

    for instruction in instructions:
        _, cnt, _, src, _, dst = instruction.split(' ')
        cnt = int(cnt)

        src_idx = col_idxs[int(src)-1]
        dst_idx = col_idxs[int(dst)-1]

        # 1
        for i in range(0, cnt):
            x = cols[src_idx].pop()
            cols[dst_idx].append(x)

        # 2
        x = cols2[src_idx][-cnt:]
        cols2[src_idx] = cols2[src_idx][:-cnt]
        cols2[dst_idx].extend(x)

    print(''.join(list(map(lambda key: cols[key][-1], cols.keys()))))
    print(''.join(list(map(lambda key: cols2[key][-1], cols.keys()))))

