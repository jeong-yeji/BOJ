for t in range(int(input())):
    n = int(input())
    cnt = 0
    isCounted = [False] * 10
    while sum(isCounted) != 10:
        cnt += 1
        for i in str(n * cnt):
            isCounted[int(i)] = True
    print(f'#{t + 1} {cnt * n}')
