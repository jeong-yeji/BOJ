import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input_two_numbers = lambda: map(int, sys.stdin.readline().strip().split())


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m = input_two_numbers()
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = input_two_numbers()
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n + 1)
answer = 0
for i in range(1, n + 1):
    if not visited[i]:
        answer += 1
        bfs(graph, i, visited)
        # dfs(graph, i, visited)

print(answer)
