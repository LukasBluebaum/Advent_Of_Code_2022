import re

def dfs(b, t, ro, rc, robs, rg, o, c, obs, dp):
    key = (t, ro, rc, robs, min(o, max(b[0], b[1], b[2][0], b[3][0]) * 2),
           min(c, b[2][1] * 2), min(obs, b[3][1]*2))
    if t == 24:
        return 0
    if key in dp:
        return dp[key]

    count = 0
    if o >= b[3][0] and obs >= b[3][1]:
        count = max(count, rg + dfs(b, t+1, ro, rc, robs, rg+1,
                                    o - b[3][0] + ro, c + rc, obs - b[3][1] + robs, dp))
    else:
        count = max(count, rg + dfs(b, t+1, ro, rc, robs, rg,
                                    o + ro, c + rc, obs + robs, dp))

        if o >= b[2][0] and c >= b[2][1] and robs < b[3][1]:
            count = max(count, rg + dfs(b, t+1, ro, rc, robs+1, rg,
                                        o - b[2][0] + ro, c - b[2][1] + rc, obs + robs, dp))
        if o >= b[1] and rc < b[2][1]:
            count = max(count, rg + dfs(b, t+1, ro, rc+1, robs, rg,
                                        o - b[1] + ro, c + rc, obs + robs, dp))
        if o >= b[0] and ro < max(b[0], b[1], b[2][0], b[3][0]):
            count = max(count, rg + dfs(b, t+1, ro+1, rc, robs, rg,
                                        o - b[0] + ro, c + rc, obs + robs, dp))

    dp[key] = count
    return count

with open("in.txt") as file:
    lines = file.readlines()

prints = [re.findall(r'\d+', line) for line in lines]
prints = [[int(p[1]), int(p[2]), (int(p[3]), int(p[4])), ((int(p[5]), int(p[6])))]
          for p in prints]

res = 0
for idx, b in enumerate(prints):
    val = dfs(b, 0, 1, 0, 0, 0, 0, 0, 0, {})
    print(val)
    res += val * (idx + 1)
print(res)
