import sys


def dfs(x, y, depth, total):
    global answer
    if depth == 4:
        answer = max(answer, total)
        return
    if total + maximum * (4 - depth) <= answer:
        return
    
    for dx, dy in delta:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
            continue
        if depth == 2:
            visited[nx][ny] = 1
            dfs(x, y, depth + 1, total + board[nx][ny])
            visited[nx][ny] = 0
        visited[nx][ny] = 1
        dfs(nx, ny, depth + 1, total + board[nx][ny])
        visited[nx][ny] = 0


input = lambda: sys.stdin.readline().strip()
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
maximum = max(map(max, board))
visited = [[0] * m for _ in range(n)]
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
answer = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, board[i][j])
        visited[i][j] = 0
print(answer)
