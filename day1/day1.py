with open('input1') as f:
    current = 0
    o = []
    for line in f:
        if len(line.strip()) == 0:
            o.append(current)
            current = 0
        else:
            current += int(line.strip())
    print(sum(sorted(o)[-3:]))

