
def has_duplicates(window):
    return len(window) != len(set(window))

def find_marker(line, window_size):
    line = [*line]

    window = line[0:window_size]

    for i in range(window_size, len(line)):
        if not has_duplicates(window):
            return i
        window.pop(0)
        window.append(line[i])

with open('input.txt') as f:
    content = map(lambda x: x.strip(), f.readlines())

    for line in content:
        marker = find_marker(line, window_size=4)
        print(marker)
        marker = find_marker(line, window_size=14)
        print(marker)

