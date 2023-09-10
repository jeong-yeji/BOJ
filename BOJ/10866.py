# 덱
from collections import deque
import sys

input = sys.stdin.readline

dq = deque()
for _ in range(int(input().rstrip())):
    cmd = input().rstrip()

    if cmd.startswith("push_front"):
        dq.appendleft(int(cmd[11:]))
    elif cmd.startswith("push_back"):
        dq.append(int(cmd[10:]))
    elif cmd == "pop_front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif cmd == "pop_back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif cmd == "size":
        print(len(dq))
    elif cmd == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    else:  # back
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[len(dq) - 1])
