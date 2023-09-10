for t in range(int(input())):
    n, m = map(int, input().split())
    list_n = list(map(int, input().split()))
    list_m = list(map(int, input().split()))

    if n > m:
        n, m = m, n
        list_n, list_m = list_m, list_n

    res = 0
    for i in range(m - n + 1):
        s = 0
        for j in range(n):
            s += (list_n[j] * list_m[i + j])
        res = max(res, s)
        
    print(f'#{t + 1} {res}')
