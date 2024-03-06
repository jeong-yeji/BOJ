import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, visited):
    queue = deque([x])
    while queue:
        i = queue.popleft()
        for j in graph[i]:
            if not visited[j]:
                queue.append(j)
                visited[j] = 1


def dfs(p, visited):
    for q in graph[p]:
        if not visited[q]:
            visited[q] = 1
            dfs(q, visited)


n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    for j, v in enumerate(map(int, input().split())):
        if v:
            graph[i].append(j)

for i in range(n):
    visited = [0] * n
    # bfs(i, visited)
    dfs(i, visited)
    print(' '.join(map(str, visited)))
