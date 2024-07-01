import re

with open('in.txt') as file:
    lines = file.readlines()

order = [(idx, 811589153 * int(re.findall(r'^-?\d+', line)[0])) for idx, line in enumerate(lines)]
nums = list(order)

for _ in range(10):
    for i, num in order:
        for idx, (k, n) in enumerate(nums):
            if k == i:
                break
        del nums[idx]
        nidx = (num + idx) % len(nums)
        nums.insert(nidx, (k, n))

i = 0
for idx, (k, n) in enumerate(nums):
    if n == 0:
        i = idx
        break

res = 0
for n in [1000, 2000, 3000]:
    res += nums[((n + i) % len(nums))][1]
print(res)


