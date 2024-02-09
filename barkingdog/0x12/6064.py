import math

for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    if x == m:
        x = 0
    if y == n:
        y = 0

    for i in range(x, math.lcm(m, n) + 1, m):
        if i == 0:
            continue
        if i % n == y:
            print(i)
            break
    else:
        print(-1)
