

'''
with open('input.txt') as f:
    lines = [line.strip() for line in f]

parts = [(set(line[:len(line)//2]), set(line[len(line)//2:])) for line in lines]

count = 0
for a ,b in parts:
    c = list(a & b)[0]
    if c.islower():
        count += ord(c) - 97 + 1
    else:
        count += ord(c) - 65 + 27

print(count)
'''

with open('input.txt') as f:
    lines = [set(line.strip()) for line in f]

count = 0
for i in range(0, len(lines)-2, 3):
    c = list(lines[i] & lines[i+1] & lines[i+2])[0]
    if c.islower():
        count += ord(c) - 97 + 1
    else:
        count += ord(c) - 65 + 27
print(count)

