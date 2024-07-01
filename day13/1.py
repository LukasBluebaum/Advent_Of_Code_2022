from functools import cmp_to_key


with open('in.txt') as file:
    lines = file.readlines()

lines = [eval(line.strip()) for line in lines if len(line) > 2]
pairs = [(a, b) for a, b in zip(lines[::2], lines[1::2])]

def cmp(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

def check(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return cmp(a, b)
    elif isinstance(a, int):
        a = [a]
    elif isinstance(b, int):
        b = [b]

    for left, right in zip(a, b):
        tmp = check(left, right)
        if tmp != 0:
            return tmp

    return cmp(len(a), len(b))

print(sum(idx+1 for idx, (a, b) in enumerate(pairs) if check(a, b) == -1))

lines.append([[2]])
lines.append([[6]])
lines = sorted(lines, key=cmp_to_key(check))
print((lines.index([[2]])+1) * (lines.index([[6]])+1))

