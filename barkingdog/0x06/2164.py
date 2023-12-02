from collections import deque

queue = deque(list(range(1, int(input()) + 1)))
while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue.pop())
