from collections import deque
from itertools import combinations


def is_valid(idxes):
    if sum(board[x][y] == 'Y' for x, y in idxes) > 3:
        return False

    vis = [[True] * 5 for _ in range(5)]
    for x, y in idxes[1:]:
        vis[x][y] = False

    cnt = 1
    queue = deque([idxes[0]])
    while queue:
        x, y = queue.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and not vis[nx][ny]:
                cnt += 1
                vis[nx][ny] = True
                queue.append((nx, ny))

    return cnt == 7


board = [list(input()) for _ in range(5)]
indexes = [(i, j) for i in range(5) for j in range(5)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
print(sum(1 for comb in combinations(indexes, 7) if is_valid(comb)))
