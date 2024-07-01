from collections import deque

def check(grid, m, i, j):
    for p in range(len(grid[0])):
        k = grid[i][p]
        if k == '>' and j == ((p + m) % len(grid[0])):
            return False
        elif k == '<' and j == ((p - m) % len(grid[0])):
            return False

    for p in range(len(grid)):
        k = grid[p][j]
        if k == 'v' and i == ((p + m) % len(grid)):
            return False
        elif k == '^' and i == ((p - m) % len(grid)):
            return False
    return True


def bfs(lines, start, end, time):
    queue = deque()
    queue.append((start[0], start[1], time))
    visited = set()
    visited.add((start[0], start[1], time))

    while len(queue) > 0:
        i, j, d = queue.popleft()

        for di, dj in [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni = i + di
            nj = j + dj
            if ni == end[0] and nj == end[1]:
                return d + 1
            if ni == start[0] and nj == start[1] and (ni, nj, d+1) not in visited:
                visited.add((ni, nj, d+1))
                queue.append((ni, nj, d+1))
                continue
            if ni < 0 or nj < 0 or ni >= m or nj >= n or (ni, nj, d+1) in visited \
                    or not check(lines, d+1, ni, nj):
                continue
            visited.add((ni, nj, d+1))
            queue.append((ni, nj, d+1))

with open('in.txt') as file:
    lines = file.readlines()

lines = [[l for l in line[1:-2]] for line in lines[1:-1]]
m = len(lines)
n = len(lines[0])

t1 = bfs(lines, (-1, 0), (m, n-1), 0)
print(t1)
t2 = bfs(lines, (m, n-1), (-1, 0), t1+1)
print(t2)
t3 = bfs(lines, (-1, 0), (m, n-1), t2+1)
print(t3)
