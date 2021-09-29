# 터렛
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    if d == 0 and r1 == r2:
        print(-1)
    elif r1 + r2 == d or abs(r1 - r2) == d:
        print(1)
    elif r1 + r2 < d or abs(r1 - r2) > d:
        print(0)
    else:
        print(2)