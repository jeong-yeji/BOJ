n, c = map(int, input().split())
d = {}
for number in map(int, input().split()):
    d[number] = d.get(number, 0) + 1
for val, cnt in sorted(d.items(), key=lambda x: -x[1]):
    for _ in range(cnt):
        print(val, end=" ")
