import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


def DFS(start, visited, graph, group):
    visited[start] = group
    for v in graph[start]:
        if visited[v]:
            if visited[v] == group:
                return False
        else:
            if not DFS(v, visited, graph, -group):
                return False
    return True


def sol_dfs(V):
    visited = [0] * (V + 1)
    for i in range(1, V + 1):
        if not visited[i]:
            if not DFS(i, visited, graph, 1):
                return "NO"
    return "YES"


def sol_bfs(V, graph):
    queue = deque([])
    visited = [0] * (V + 1)
    for node in range(V):
        if not visited[node]:
            visited[node] = 1
            queue.append(node)
            while queue:
                i = queue.popleft()
                for j in graph[i]:
                    if not visited[j]:
                        visited[j] = -visited[i]
                        queue.append(j)
                    elif visited[j] == visited[i]:
                        return "NO"
    return "YES"


for _ in range(int(input())):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    print(sol_dfs(V))
    print(sol_bfs(V, graph))
