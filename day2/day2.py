with open('input1.txt') as f:
    inp = [line.strip().split() for line in f]


count = 0

for i in inp:
    x = i[0]
    y = i[1]
    if y == 'X':
        if x == 'A':
            count += 3
        elif x == 'B':
            count += 1
        else:
            count += 2
    elif y == 'Y':
        count += 3
        if x == 'A':
            count += 1
        elif x == 'B':
            count += 2
        else:
            count += 3
    else:
        count += 6
        if x == 'A':
            count += 2
        elif x == 'B':
            count += 3
        else:
            count += 1

print(count)


