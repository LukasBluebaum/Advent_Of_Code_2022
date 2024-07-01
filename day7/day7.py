from typing import List
from dataclasses import dataclass
import re


@dataclass
class Dir:
    name: str
    size: int
    parent: 'Dir'
    childs: List['Dir']


with open('input.txt') as f:
    lines = [line.strip() for line in f]

current = Dir(lines[0], 0, None, [])
sizes = []

for line in lines[1:]:
    if line.startswith('$ cd'):
        if '..' in line:
            sizes.append(current.size)
            temp_size = current.size
            current = current.parent
            current.size += temp_size
        else:
            temp_dir = Dir(line, 0, current, [])
            current.childs.append(temp_dir)
            current = temp_dir
    else:
        x = re.findall(r'^\d+', line)
        if len(x) == 1:
            current.size += int(x[0])


while current.parent is not None:
    sizes.append(current.size)
    temp_size = current.size
    current = current.parent
    current.size += temp_size
sizes.append(current.size)

print(sum(s for s in sizes if s < 100000))
target = 30000000 - (70000000 - current.size)
print(min(s for s in sizes if s > target))

