from collections import defaultdict


with open('in.txt') as f:
    lines = f.readlines()

d = {
    'N': [(-1, 0), (-1, 1), (-1, -1)],
    'S': [(1, 0), (1, 1), (1, -1)],
    'W': [(0, -1), (-1, -1), (1, -1)],
    'E': [(0, 1), (-1, 1), (1, 1)],
}


def find_pos(a, b, direction, pos):
    count = 0
    for key in direction:
        for di, dj in d[key]:
            if (a + di, b + dj) in pos:
                count += 1
    if count == 0:
        return a, b

    for key in direction:
        for di, dj in d[key]:
            if (a + di, b + dj) in pos:
                break
        else:
            return a + d[key][0][0], b + d[key][0][1]
    return a, b


def round_(pos, direction):
    tmp = set()
    proposals = defaultdict(list)
    for a, b in pos:
        proposals[find_pos(a, b, direction, pos)].append((a, b))

    for new_pos in proposals:
        if len(proposals[new_pos]) == 1:
            tmp.add(new_pos)
        else:
            tmp.update(proposals[new_pos])

    direction = direction[1:] + [direction[0]]
    return tmp, direction, tmp == pos


def find_reactangle(pos):
    min_row, max_row = float('inf'), float('-inf')
    min_col, max_col = float('inf'), float('-inf')
    for a, b in pos:
        min_row = min(min_row, a)
        max_row = max(max_row, a)
        min_col = min(min_col, b)
        max_col = max(max_col, b)
    return (max_row - min_row + 1) * (max_col - min_col + 1) - len(pos)


pos = set([(a, b) for a in range(len(lines)) for b in range(len(lines[0]))
       if lines[a][b] == '#'])
direction = ['N', 'S', 'W', 'E']

rounds = 10**4
for i in range(rounds):
    pos, direction, moved = round_(pos, direction)
    if moved:
        print(i+1)
        break

