n = int(input())
times = list(map(int, input().split()))

y, m = 0, 0
for time in times:
    y += 10 * (time // 30 + 1)
    m += 15 * (time // 60 + 1)

if y > m:
    print(f"M {m}")
elif y < m:
    print(f"Y {y}")
elif y == m:
    print(f"Y M {y}")
