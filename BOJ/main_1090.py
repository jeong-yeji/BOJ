import sys

n = int(input())

points = []
point_x = []
point_y = []
answer = [sys.maxsize] * n

for _ in range(n):
    y, x = map(int, input().split())
    points.append([x, y])
    point_x.append(x)
    point_y.append(y)

for y in point_y:
    for x in point_x:
        dist = []

        for a, b in points:
            d = abs(a - x) + abs(b - y)
            dist.append(d)

        dist.sort()

        tmp = 0
        for i, d in enumerate(dist):
            tmp += d
            answer[i] = min(tmp, answer[i])

print(*answer)
