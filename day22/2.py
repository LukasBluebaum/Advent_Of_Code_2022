from collections import defaultdict
import re

with open("test.txt") as file:
    lines = file.readlines()

with open("test_path.txt") as file:
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
    if d == 0 and pos[1] + 1 <= ends_rows[i]:
        return (pos[0], pos[1] + 1), d
    elif d == 1 and pos[0] + 1 <= ends_cols[j]:
        return (pos[0] + 1, pos[1]), d
    elif d == 2 and pos[1] - 1 >= starts_rows[i]:
        return (pos[0], pos[1] - 1), d
    elif d == 3 and pos[0] - 1 >= starts_cols[j]:
        return (pos[0] - 1, pos[1]), d

    if i == 0 and d == 3:
        return (i + 4,  , 1




path = re.findall(r'(\d+|\w)', path)

# R, D, L, U
dir_ = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0

pos = (0, starts_rows[0])
for p in path:
    if p == 'R':
        d = (d + 1) % len(dir_)
    elif p == 'L':
        d = (d - 1) % len(dir_)
    else:
        p = int(p)
        while p > 0:
            new_pos, new_d = get_next(pos, d)
            if points[new_pos] == '#':
                break
            pos = new_pos
            d = new_d
            p -= 1

print(pos, d)
print((pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + d)




