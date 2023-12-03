import sys

stack = []
for _ in range(int(input())):
    cmd = sys.stdin.readline().rstrip().split()

    if cmd[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        print(int(len(stack) == 0))
    elif cmd[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    else:
        stack.append(cmd[1])
