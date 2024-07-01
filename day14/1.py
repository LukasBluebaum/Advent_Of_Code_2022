
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

def limits(grid):
    min_x, max_x = float('inf'), 0
    for i, j in grid:
        min_x = min(i, min_x)
        max_x = max(i, max_x)
    return min_x, max_x


def fall(grid, min_x, max_x):
    down = lambda a: (a[0], a[1] + 1)
    left = lambda a: (a[0]-1, a[1] + 1)
    right = lambda a: (a[0]+1, a[1] + 1)

    pos = (500, 0)
    while True:
        d = down(pos)
        l = left(pos)
        r = right(pos)
        if d in grid and l in grid and r in grid:
            return pos
        elif d in grid and l in grid:
            pos = r
        elif d in grid:
            pos = l
        else:
            pos = d
        if pos[0] < min_x or pos[0] > max_x:
            return None


with open("in.txt") as file:
    lines = file.readlines()

grid = set()
for line in lines:
    grid.update(get_coords([tuple(int(c) for c in coords.strip().split(","))
                            for coords in line.split("->")]))


min_x, max_x = limits(grid)

c = 0
while True:
   pos = fall(grid, min_x, max_x)
   if pos is None:
       break
   grid.add(pos)
   c += 1
print(c)

