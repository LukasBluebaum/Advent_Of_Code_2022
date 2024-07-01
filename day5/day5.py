import re

with open('input.txt') as f:
    lines = [line for line in f]

lists = []
commands = []
for idx, line in enumerate(lines):
    if line.startswith('move'):
        commands.append(re.findall(r'\d+', line))
    elif len(re.findall(r'\d+', line)) == 0 and len(line.strip()) != 0:
        x = re.findall(r'(\w+|    )', line)
        lists.append(x)


stacks = [[] for _ in range(len(lists[-1]))]
for l in lists:
    for idx, x in enumerate(l):
        if len(x.strip()) != 0:
            stacks[idx].insert(0, x)

print(stacks)
for idx, c in enumerate(commands):
    amount = int(c[0])
    from_ = int(c[1])
    target = int(c[2])
    stacks[target-1] += stacks[from_-1][-amount:]
    #stacks[target-1] += stacks[from_-1][-amount:][::-1]
    del stacks[from_-1][-amount:]

print("".join([l[-1] for l in stacks]))

