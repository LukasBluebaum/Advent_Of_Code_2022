
def get_max(grid):
    return max(a for a, _ in grid)


def remove(grid):
    m = [float('-inf')] * 7
    for a, b in grid:
        m[b] = max(m[b], a)
    m = min(m)
    to_remove = set()
    for a, b in grid:
        if a < m:
            to_remove.add((a, b))
    grid -= to_remove
    return grid


def drift(grid, stone, direction):
    move = lambda a: 1 if a == '>' else -1
    db = move(direction)
    new_pos = [(a, b + db) for a, b in stone]
    if any(b < 0 or b > 6 for _, b in new_pos) or any((a, b) in grid for a, b in new_pos):
        return stone
    else:
        return new_pos


def fall(grid, stone):
    new_pos = [(a-1, b) for a, b in stone]
    if any((a, b) in grid for a, b in new_pos):
        return stone, False
    else:
        return new_pos, True


def round_(grid, stones, directions, current_s, current_d):
    m = get_max(grid)
    stone = stones[current_s]
    stone = [(a + m + 4, b) for a, b in stone]

    while True:
        direction = directions[current_d]
        current_d = (current_d + 1) % len(directions)
        stone = drift(grid, stone, direction)
        new_pos, worked = fall(grid, stone)
        if not worked:
            break
        else:
            stone = new_pos

    grid.update(stone)
    return current_d


with open("in.txt") as file:
    lines = file.readlines()

directions = lines[0].strip()

stones = [
    [(0, 2), (0, 3), (0, 4), (0, 5)],
    [(0, 3), (1, 2), (1, 3), (1, 4), (2, 3)],
    [(0, 2), (0, 3), (0, 4), (1, 4), (2, 4)],
    [(0, 2), (1, 2), (2, 2), (3, 2)],
    [(0, 2), (0, 3), (1, 2), (1, 3)],
]

grid = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)}

rounds = 10**12
current_d = 0
current_s = 0

seen = {}
heights = {}
i = 0
while i < rounds:
    current_d = round_(grid, stones, directions, current_s, current_d)
    current_s = (current_s + 1) % len(stones)
    grid = remove(grid)
    i += 1

    m = get_max(grid)
    key = (frozenset((g[0]-m, g[1]) for g in grid), current_d, current_s)
    if key in seen:
        pos = seen[key]
        height = heights[pos]
        circle = i - pos
        number_circles = (rounds - pos) // circle

        remaining = heights[pos + (rounds - pos) % circle]
        h = number_circles * (m - height) + remaining
        print(h)
        break
    else:
        seen[key] = i
        heights[i] = m

