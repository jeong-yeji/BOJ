def dfs(depth, idx):
    global result, n
    if depth == n // 2:
        s = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    s += arr[i][j]
                elif not visited[i] and not visited[j]:
                    s -= arr[i][j]
        result = min(result, abs(s))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
result = 1e9
dfs(0, 0)
print(result)
