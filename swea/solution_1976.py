for t in range(int(input())):
    hour1, min1, hour2, min2 = map(int, input().split())
    h, m = divmod(min1 + min2, 60)
    h = (h + hour1 + hour2) % 12
    if h == 0:
        h = 12
    print(f'#{t + 1} {h} {m}')
