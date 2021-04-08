# 균형잡힌 세상
import sys

while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".":
        break
    stack = []
    flag = 1

    for s in sentence:
        if s in "([":
            stack.append(s)
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = 0
                break
        elif s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                flag = 0
                break

    print("yes" if flag and len(stack) == 0 else "no")
