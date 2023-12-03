import sys

while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".":
        break

    stack = []
    flag = True

    for s in sentence:
        if s in "([":
            stack.append(s)
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = False
                break
        elif s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                flag = False
                break

    if len(stack) != 0:
        flag = False

    print("yes" if flag else "no")
