import re
import math
from collections import defaultdict

with open('in.txt') as file:
    lines = file.readlines()

graph = {line.split(':')[0]: line.split(':')[1] for line in lines}

def dfs(current):
    num = re.findall(r'\d+', graph[current])
    if len(num) > 0:
        return int(num[0])

    op = re.findall(r'[\+\-*/]', graph[current])[0]
    nbs = re.findall(r'\w+', graph[current])
    if current == 'root':
        tmp1 = dfs(nbs[0])
        tmp2 = dfs(nbs[1])
        return tmp1 == tmp2, tmp1, tmp2
    if op == '*':
        return dfs(nbs[0]) * dfs(nbs[1])
    elif op == '+':
        return dfs(nbs[0]) + dfs(nbs[1])
    elif op == '-':
        return dfs(nbs[0]) - dfs(nbs[1])
    else:
        return dfs(nbs[0]) / dfs(nbs[1])

l = 0
r = 10**20
while l <= r:
    mid = l + (r - l) // 2
    graph['humn'] = str(mid)
    equal, a, b = dfs('root')
    if equal:
        print(mid)
        break
    elif a < b:
        r = mid - 1
    else:
        l = mid + 1


