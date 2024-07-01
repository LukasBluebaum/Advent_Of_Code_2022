from itertools import takewhile

with open('input.txt') as f:
    matrix = [list(map(int, list(line.strip()))) for line in f]

'''
count = 0
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        current = matrix[row][col]
        if row == 0 or col == 0 or row == len(matrix)-1 or col == len(matrix[0])-1:
            count += 1
        elif max(matrix[row][:col]) < current or \
             max(matrix[row][col+1:]) < current or \
             max([matrix[i][col] for i in range(row)]) < current or \
             max([matrix[i][col] for i in range(row+1, len(matrix))]) < current:
            count += 1

print(count)
'''
c = 0
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        current = matrix[row][col]
        if row == 0 or col == 0 or row == len(matrix)-1 or col == len(matrix[0])-1:
            continue
        i1 = sum(1 for i in takewhile(lambda x: x < current, matrix[row][:col][::-1]))
        i1 += int(len(matrix[row][:col]) != i1)
        i2 = sum(1 for i in takewhile(lambda x: x < current, matrix[row][col+1:]))
        i2 += int(len(matrix[row][col+1:]) != i2)
        i3 = sum(1 for i in takewhile(lambda x: x < current, [matrix[i][col] for i in range(row)][::-1]))
        i3 += int(len([matrix[i][col] for i in range(row)]) != i3)
        i4 = sum(1 for i in takewhile(lambda x: x < current, [matrix[i][col] for i in range(row+1, len(matrix))]))
        i4 += int(len([matrix[i][col] for i in range(row+1, len(matrix))]) != i4)
        c = max(i1*i2*i3*i4, c)

print(c)
