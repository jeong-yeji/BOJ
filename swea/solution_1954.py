dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for t in range(int(input())):
    n = int(input())
    cnt, d, x, y = 1, 0, 0, 0
    snail = [[0 for _ in range(n)] for _ in range(n)]

    while cnt <= n * n:
        snail[x][y] = cnt

        next_x = x + dr[d]
        next_y = y + dc[d]
        if not (0 <= next_x < n and 0 <= next_y < n and snail[next_x][next_y] == 0):
            d = (d + 1) % 4

        x += dr[d]
        y += dc[d]
        cnt += 1

    print(f'#{t + 1}')
    for line in snail:
        print(' '.join(map(str, line)))
