from collections import deque

with open('in.txt') as file:
    lines = file.readlines()

lines = [list(line.strip()) for line in lines]

end = None
queue = deque()
visited = set()
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 'S':
            lines[i][j] = 'a'
        if lines[i][j] == 'E':
            lines[i][j] = 'z'
            end = (i, j)
        if lines[i][j] == 'a':
            queue.append(((i, j), 0))
            visited.add((i, j))


while len(queue) > 0:
    (i, j), d = queue.popleft()
    if (i, j) == end:
        print(d)
        break

    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ni = i + di
        nj = j + dj

        if ni < 0 or nj < 0 or ni >= len(lines) or nj >= len(lines[0]):
            continue

        if (ni, nj) not in visited and ord(lines[ni][nj]) - ord(lines[i][j]) <= 1:
            visited.add((ni, nj))
            queue.append(((ni, nj), d+1))
