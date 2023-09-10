# 카드2
from collections import deque

n = int(input())
numqueue = deque([i for i in range(1, n + 1)])
while len(numqueue) > 1:
    numqueue.popleft()
    numqueue.append(numqueue.popleft())
print(*numqueue)
