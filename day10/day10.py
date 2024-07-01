
cycles = {20, 60, 100, 140, 180, 220}

def check_signal(x, c):
    if c in cycles:
        print(c*x)
        return c*x
    else:
        return 0

def set_sprite(sprite, x, c):
    row = c // 40
    col = c % 40
    if col <= x+1 and col >= x-1:
        sprite[row][col] = '#'


with open('input.txt') as f:
    lines = [line.strip().split(' ') for line in f]


sprite = [['.']*40 for _ in range(6)]

x = 1
c = 0
sum_ = 0
for line in lines:
    set_sprite(sprite, x, c)
    c += 1
    sum_ += check_signal(x, c)
    if line[0] == 'addx':
        set_sprite(sprite, x, c)
        c += 1
        sum_ += check_signal(x, c)
        x += int(line[1])


print(sum_)
[print(''.join(x)) for x in sprite]

