n, k = map(int, input().split())
dp = [True] * (n + 1)
dp[0] = dp[1] = False
for i in range(2, n + 1):
    if not dp[i]:
        continue
        
    for j in range(i, n + 1, i):
        if dp[j]:
            k -= 1
            dp[j] = False
            if k == 0:
                print(j)
