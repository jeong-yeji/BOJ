for i in range(int(input())):
    a, b = map(int, input().split())
    res = '='
    if a > b:
        res = '>'
    elif a < b:
        res = '<'
    print(f'#{i + 1} {res}')
