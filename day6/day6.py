from collections import deque


with open('input.txt') as f:
    line = f.readlines()[0].strip()


q = deque()
for idx, c in enumerate(line):
    if len(q) == 14:
        x = q.popleft()
    q.append(c)
    if len(set(q)) == 14:
        print(idx + 1)
        break


