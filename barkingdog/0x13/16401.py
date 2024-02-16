m, n = map(int, input().split())
snacks = list(map(int, input().split()))
s, e = 0, 1_000_000_000
while s < e:
    mid = (s + e + 1) // 2
    if sum(snack // mid for snack in snacks) >= m:
        s = mid
    else:
        e = mid - 1
print(s)
