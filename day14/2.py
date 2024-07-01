
def get_coords(line):
    coords = set()
    for i in range(len(line)-1):
        a, b = line[i], line[i+1]
        if a[0] == b[0]:
            x, y = min(a[1], b[1]), max(a[1], b[1])
            coords.update((a[0], k) for k in range(x, y+1))
        else:
            x, y = min(a[0], b[0]), max(a[0], b[0])
            coords.update((k, a[1]) for k in range(x, y+1))
    return coords

def fall(grid, max_y):
    down = lambda a: (a[0], a[1] + 1)
    left = lambda a: (a[0]-1, a[1] + 1)
    right = lambda a: (a[0]+1, a[1] + 1)

    pos = (500, 0)
    while True:
        d = down(pos)
        l = left(pos)
        r = right(pos)
        dd = (d in grid or d[1] == max_y)
        ll = (l in grid or l[1] == max_y)
        rr = (r in grid or r[1] == max_y)
        if dd and ll and rr:
            return pos
        elif dd and ll:
            pos = r
        elif dd:
            pos = l
        else:
            pos = d


with open("in.txt") as file:
    lines = file.readlines()

grid = set()
for line in lines:
    grid.update(get_coords([tuple(int(c) for c in coords.strip().split(","))
                            for coords in line.split("->")]))

max_y = max(j for _, j in grid) + 2

c = 1
while True:
   pos = fall(grid, max_y)
   if pos == (500, 0):
       break
   grid.add(pos)
   c += 1
print(c)

