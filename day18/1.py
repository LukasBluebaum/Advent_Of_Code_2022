
def check(a, b):
    ah, aw, ad = a
    bh, bw, bd = b

    if ah == bh and aw == bw and abs(int(ad) - int(bd)) == 1:
        return 2
    if ah == bh and ad == bd and abs(int(aw)- int(bw)) == 1:
        return 2
    if aw == bw and ad == bd and abs(int(ah) - int(bh)) == 1:
        return 2
    return 0

with open('in.txt') as file:
    lines = file.readlines()

cubes = [line.strip().split(',') for line in lines]

res = 0
for i in range(len(cubes)):
    for j in range(i+1, len(cubes)):
        res += check(cubes[i], cubes[j])

print(len(cubes) * 6 - res)
