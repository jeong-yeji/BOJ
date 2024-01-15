import sys
from itertools import permutations

input = lambda: sys.stdin.readline().strip()
innings = [list(map(int, input().split())) for _ in range(int(input()))]
answer = 0
for lineup in permutations(range(1, 9)):
    lineup = list(lineup[:3]) + [0] + list(lineup[3:])
    cur, points = 0, 0
    for inning in innings:
        out, f, s, t = 0, 0, 0, 0
        while out < 3:
            hit = inning[lineup[cur]]
            if hit == 0:
                out += 1
            elif hit == 1:
                points += t
                f, s, t = 1, f, s
            elif hit == 2:
                points += s + t
                f, s, t = 0, 1, f
            elif hit == 3:
                points += f + s + t
                f, s, t = 0, 0, 1
            elif hit == 4:
                points += f + s + t + 1
                f, s, t = 0, 0, 0
            cur = (cur + 1) % 9
    answer = max(answer, points)
print(answer)
