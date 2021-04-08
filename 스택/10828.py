# 스택
import sys


class Stack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.isEmpty():
            return -1
        return self.data.pop()

    def peek(self):
        if self.isEmpty():
            return -1
        return self.data[-1]


intStack = Stack()
for _ in range(int(input())):
    cmd = sys.stdin.readline().rstrip()

    if cmd == "pop":
        print(intStack.pop())
    elif cmd == "size":
        print(intStack.size())
    elif cmd == "empty":
        print(intStack.isEmpty())
    elif cmd == "top":
        print(intStack.peek())
    else:  # push X
        n = int(cmd[5:])
        intStack.push(n)


stack = []
for _ in range(int(input())):
    cmd = sys.stdin.readline().rstrip()

    if cmd == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    else:
        stack.append(int(cmd[5:]))