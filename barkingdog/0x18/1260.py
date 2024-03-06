import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(graph, i, visited):
    visited[i] = True
    dfs_list.append(i)
    for j in sorted(graph[i]):
        if not visited[j]:
            dfs(graph, j, visited)


def bfs(graph, cur, visited):
    queue = deque([cur])
    visited[cur] = True
    while queue:
        i = queue.popleft()
        bfs_list.append(i)
        for j in sorted(graph[i]):
            if not visited[j]:
                queue.append(j)
                visited[j] = True


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

dfs_list, bfs_list = [], []
dfs(graph, v, [False] * (n + 1))
bfs(graph, v, [False] * (n + 1))

print(*dfs_list)
print(*bfs_list)
