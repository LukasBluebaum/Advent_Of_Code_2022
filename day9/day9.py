with open('input.txt') as f:
    lines = [line.strip().split(" ") for line in f]

commands = {'R': 1, 'L': -1, 'U': 1j, 'D': -1j}

#h = complex(0);
#t = complex(0);
rope = [complex(0) for _ in range(10)]
found = [{complex(0)} for _ in range(10)]

for line in lines:
    c = commands[line[0]]
    steps = int(line[1])
    for _ in range(steps):
        rope[0] += c
        found[0].add(rope[0])
        for p in range(1, 10):
            difference = rope[p-1] - rope[p]
            if abs(difference) >= 2:
                # compute direction
                rope[p] += complex((difference.real > 0) - (difference.real < 0),
                                   (difference.imag > 0) - (difference.imag < 0))
                found[p].add(rope[p])

print([len(f) for f in found])
