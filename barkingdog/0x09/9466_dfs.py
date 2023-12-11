import sys

input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10 ** 8)


def dfs(idx):
    global cnt
    vis[idx] = True
    cycle.append(idx)

    nxt = choices[idx]
    if vis[nxt]:
        if nxt in cycle:
            cnt -= len(cycle[cycle.index(nxt):])
        return
    dfs(nxt)


for _ in range(int(input())):
    n = int(input())
    choices = [0] + list(map(int, input().split()))
    vis = [False] * (n + 1)
    cnt = n

    for i in range(1, n + 1):
        if not vis[i]:
            cycle = []
            dfs(i)

    print(cnt)
