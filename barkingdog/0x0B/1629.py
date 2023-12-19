def recur(x, y, m):
    if y == 1:
        return x % m
    if y % 2 == 0:
        return (recur(x, y // 2, c) ** 2) % m
    return ((recur(x, y // 2, c) ** 2) * x) % m


a, b, c = map(int, input().split())
print(recur(a, b, c))
