from collections import defaultdict
import re

with open("in.txt") as file:
    lines = file.readlines()

with open("in_path.txt") as file:
    path = file.readlines()[0].strip()

lines = [list(line) for line in lines]

starts_rows = defaultdict(lambda: float('inf'))
ends_rows = defaultdict(int)
starts_cols = defaultdict(lambda: float('inf'))
ends_cols = defaultdict(int)
points = {}
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] != '.' and lines[i][j] != '#':
            continue
        starts_rows[i] = min(starts_rows[i], j)
        ends_rows[i] = max(ends_rows[i], j)
        starts_cols[j] = min(starts_cols[j], i)
        ends_cols[j] = max(ends_cols[j], i)
        points[(i, j)] = lines[i][j]


def get_next(pos, d):
    i, j = pos
    if d == 0:
        return (i, j + 1 if j + 1 <= ends_rows[i] else starts_rows[i])
    elif d == 1:
        return (i + 1 if i + 1 <= ends_cols[j] else starts_cols[j], j)
    elif d == 2:
        return (i, j - 1 if j - 1 >= starts_rows[i] else ends_rows[i])
    elif d == 3:
        return (i - 1 if i - 1 >= starts_cols[j] else ends_cols[j], j)


path = re.findall(r'(\d+|\w)', path)

d = 0

pos = (0, starts_rows[0])
for p in path:
    if p == 'R':
        d = (d + 1) % 4
    elif p == 'L':
        d = (d - 1) % 4
    else:
        p = int(p)
        while p > 0:
            new_pos = get_next(pos, d)
            if points[new_pos] == '#':
                break
            pos = new_pos
            p -= 1
print(pos, d)
print((pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + d)




