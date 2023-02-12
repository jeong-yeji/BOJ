money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
res = [0] * len(money)
for t in range(int(input())):
    n = int(input())
    for i in range(len(money)):
        a, b = divmod(n, money[i])
        res[i] = a
        n = b

    print(f'#{t + 1}')
    print(' '.join(map(str, res)))
