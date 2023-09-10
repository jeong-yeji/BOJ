for t in range(int(input())):
    res = [0, 0]
    for i in range(1, int(input()) + 1):
        res[i % 2] += i
    print(f'#{t + 1} {res[1] - res[0]}')
