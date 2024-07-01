import re

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def closest(dist, sensor, row):
    return sensor[0] - (dist - abs(sensor[1] - row))

with open('in.txt') as file:
    lines = file.readlines()

sensors = {}
for line in lines:
    nums = re.findall(r'[\-\d]+', line)
    sensors[(int(nums[0]), int(nums[1]))] = manhattan((int(nums[0]), int(nums[1])),
                                                      (int(nums[2]), int(nums[3])))
row = 2000000
intervals = []
for sensor in sensors:
    if manhattan(sensor, (sensor[0], row)) > sensors[sensor]:
        continue
    c = closest(sensors[sensor], sensor, row)
    intervals.append(sorted([abs(c - sensor[0]) + sensor[0], sensor[0] - abs(c-sensor[0])]))

intervals = sorted(intervals)
current = intervals[0]
res = []
for i in range(1, len(intervals)):
    if intervals[i][0] > current[1]:
        res.append(current)
        current = intervals[i]
    else:
        current = (current[0], max(intervals[i][1], current[1]))
res.append(current)
print(sum(abs(a - b) for a, b in res))


