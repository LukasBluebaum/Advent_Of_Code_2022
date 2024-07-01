import re

with open('in.txt') as file:
    lines = file.readlines()

graph = {line.split(':')[0]: line.split(':')[1] for line in lines}

def dfs(current):
    num = re.findall(r'\d+', graph[current])
    if len(num) > 0:
        return int(num[0])
    op = re.findall(r'[\+\-*/]', graph[current])[0]
    nbs = re.findall(r'\w+', graph[current])
    if op == '*':
        return dfs(nbs[0]) * dfs(nbs[1])
    elif op == '+':
        return dfs(nbs[0]) + dfs(nbs[1])
    elif op == '-':
        return dfs(nbs[0]) - dfs(nbs[1])
    else:
        return dfs(nbs[0]) / dfs(nbs[1])

print(dfs('root'))


