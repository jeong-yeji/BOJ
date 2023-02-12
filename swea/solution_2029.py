for i in range(int(input())):
    a, b = map(int, input().split())
    d, m = divmod(a, b)
    print(f'#{i + 1} {d} {m}')
