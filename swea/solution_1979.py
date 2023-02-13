for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    puzzle = []
    for _ in range(n):
        puzzle.append(input().split())

    res = 0

    # 가로
    for p in puzzle:
        for i in ''.join(p).split("0"):
            if len(i) == k:
                res += 1

    # 세로
    for p in list(zip(*puzzle)):
        for i in ''.join(p).split("0"):
            if len(i) == k:
                res += 1

    print(f'#{t} {res}')