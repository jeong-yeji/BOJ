from collections import deque

n, m = map(int, input().split())
numlist = list(map(int, input().split()))
queue = deque(list(range(1, n + 1)))
cnt = 0

for num in numlist:
    r = -1 if queue.index(num) <= len(queue) // 2 else 1
    while queue[0] != num:
        queue.rotate(r)
        cnt += 1
    queue.popleft()

print(cnt)
