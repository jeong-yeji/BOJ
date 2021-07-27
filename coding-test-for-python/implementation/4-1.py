# 상하좌우


def LRUD(n, moves):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    way = ["R", "L", "D", "U"]
    x, y = 1, 1

    for move in moves:
        idx = way.index(move)
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 1 <= nx <= n and 1 <= ny <= n:
            x, y = nx, ny

    return x, y


x, y = LRUD(5, ["R", "R", "R", "U", "D", "D"])
print(x, y)
