a, b = map(int, input().split())
if a == b:
    print(0)
else:
    print(abs(b - a) - 1)
    print(*[i for i in range(min(a, b) + 1, max(a, b))])
