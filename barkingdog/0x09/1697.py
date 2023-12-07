from collections import deque

n, k = map(int, input().split())
time = [100_001] * 100_001
time[n] = 0
q = deque([n])


def bfs(cur, next):
    if next < 0 or next > 100_000:
        return

    global q, time, k
    if time[next] > time[cur] + 1:
        q.append(next)
        time[next] = time[cur] + 1


while q:
    cur = q.popleft()
    bfs(cur, cur - 1)
    bfs(cur, cur + 1)
    bfs(cur, cur * 2)

print(time[k])
