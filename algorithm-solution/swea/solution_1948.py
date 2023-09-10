last = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(int(input())):
    from_mon, from_day, to_mon, to_day = map(int, input().split())
    res = 0
    if from_mon == to_mon:
        res = to_day - from_day + 1
    else:
        for mon in range(from_mon + 1, to_mon):
            res += last[mon]
        res += last[from_mon] - from_day + 1 + to_day
    print(f'#{t + 1} {res}')
