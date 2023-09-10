for t in range(int(input())):
    n, m = map(int, input().split())
    flies = []
    for _ in range(n):
        flies.append(list(map(int, input().split())))

    res = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            killed = 0
            for k in range(m):
                for l in range(m):
                    killed += flies[i + k][j + l]
            res = max(res, killed)

    print(f'#{t + 1} {res}')
