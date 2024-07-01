import re
from collections import deque

def shortest(valves, valve):
    queue = deque()
    visited = set()
    queue.append((valve, [valve]))
    visited.add(valve)

    paths = []
    while len(queue) > 0:
        node, path = queue.popleft()
        for nb in valves[node][0]:
            if nb not in visited:
                visited.add(nb)
                queue.append((nb, path + [nb]))
                paths.append(path + [nb])
    return paths


def find(node, time, paths, valves, indices, open_, dp):
    key = (node, time, open_)
    if open_ == len(valves)**2 - 1 or time >= 30:
        return 0
    if key in dp:
        return dp[key]

    count = 0
    for path in paths[node]:
        t = time + len(path) - 1
        if not (open_ & (1 <<(indices[path[-1]]))):
            tmp = (30 - (t+1)) * valves[path[-1]][1]
            count = max(count, tmp + find(path[-1], t+1, paths,
                        valves, indices, open_ | (1 << (indices[path[-1]])), dp))
    dp[key] = count
    return count


with open("in.txt") as file:
    lines = file.readlines()

valves = {}
for line in lines:
    v = re.findall(r'[A-Z]+', line)
    rate = re.findall(r'\d+', line)
    valves[v[1]] = (v[2:], int(rate[0]))

paths = {valve: shortest(valves, valve) for valve in sorted(valves)}
indices = {v: idx for idx, v in enumerate(sorted(valves))}
open_ = 0
for v in valves:
    if valves[v][1] == 0:
        open_ = open_ | (1 << indices[v])
print(find("AA", 0, paths, valves, indices, open_, {}))

