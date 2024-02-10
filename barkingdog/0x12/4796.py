t = 0
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    t += 1
    a, b = divmod(v, p)
    b = min(b, l)
    print(f"Case {t}: {a * l + b}")
