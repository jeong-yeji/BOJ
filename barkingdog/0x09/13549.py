from collections import deque

n, k = map(int, input().split())
time = [100_001] * 100_001
time[n] = 0
q = deque([n])


def bfs(next, t):
    if next < 0 or next > 100_000:
        return

    global q, time, k
    if time[next] > t:
        q.append(next)
        time[next] = t


while q:
    cur = q.popleft()
    bfs(cur - 1, time[cur] + 1)
    bfs(cur + 1, time[cur] + 1)
    bfs(cur * 2, time[cur])

print(time[k])
