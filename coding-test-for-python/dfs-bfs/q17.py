# 경쟁적 전염

from collections import deque


def solution(n, k, tube, s, x, y):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    data = []

    for i in range(n):
        for j in range(n):
            if tube[i][j] != 0:
                data.append((tube[i][j], i, j, 0))

    data.sort()
    queue = deque(data)
    print(queue)
    while queue:
        virus, a, b, time = queue.popleft()

        if time == s:
            break

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if tube[nx][ny] == 0:
                    tube[nx][ny] = virus
                    queue.append((virus, nx, ny, time + 1))

    return tube[x - 1][y - 1], tube


tube = [[1, 0, 2], [0, 0, 0], [3, 0, 0]]
print(solution(3, 3, tube, 2, 3, 2))
print(solution(3, 3, tube, 1, 2, 2))