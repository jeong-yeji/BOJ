cnt = 0
for _ in range(int(input())):
    stack = []
    for i in input():
        if stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    if not stack:
        cnt += 1

print(cnt)
