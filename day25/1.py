
with open("in.txt") as file:
    lines = file.readlines()

res = 0
for line in lines:
    m = 1
    num = 0
    for c in reversed(line.strip()):
        if c == '-':
            num += - 1 * m
        elif c == '=':
            num += - 2 * m
        else:
            num += int(c) * m
        m *= 5
    res += num

print(res)
s = ""
while res > 0:
    r = res % 5
    if r == 0:
        s += '0'
    elif r == 1:
        s += '1'
    elif r == 2:
        s += '2'
    elif r == 3:
        s += '='
        res += 5
    elif r == 4:
        s += '-'
        res += 5

    res //= 5
print(s[::-1])

