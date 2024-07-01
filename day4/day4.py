with open('input.txt') as f:
    pairs = [line.strip().split(',') for line in f]

pairs = [(set(range(int(p[0].split('-')[0]), int(p[0].split('-')[1])+1)),
          set(range(int(p[1].split('-')[0]), int(p[1].split('-')[1])+1)))
          for p in pairs]
# part 1
#print(sum(1 for p1, p2 in pairs if len(p1-p2) == 0 or len(p2-p1) == 0))
# part 2
print(sum(1 for p1, p2 in pairs if len(p1 & p2) > 0))
