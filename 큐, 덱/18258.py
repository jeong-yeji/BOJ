# 큐 2
import sys
from collections import deque

input = sys.stdin.readline
q = deque()

for _ in range(int(input())):
    cmd = input().rstrip()
    if cmd == "front":
        print(q[0] if q else -1)
    elif cmd == "back":
        print(q[-1] if q else -1)
    elif cmd == "size":
        print(len(q))
    elif cmd == "empty":
        print(0 if q else 1)
    elif cmd == "pop":
        print(q.popleft() if q else -1)
    else:
        q.append(int(cmd[5:]))