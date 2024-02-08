import sys

input = lambda: sys.stdin.readline().strip()

flowers = []
for _ in range(int(input())):
    sm, sd, em, ed = map(int, input().split())
    flowers.append([sm * 100 + sd, em * 100 + ed])
flowers.sort()

end, cnt = 301, 0
while flowers:
    if flowers[0][0] > end or end >= 1201:
        break

    tmp = -1
    for _ in range(len(flowers)):
        if flowers[0][0] > end:
            break
        tmp = max(tmp, flowers[0][1])
        del flowers[0]

    end = tmp
    cnt += 1

print(0 if end < 1201 else cnt)
