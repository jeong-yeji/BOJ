brackets = input()
res, tmp = 0, 1
stack = []
for i in range(len(brackets)):
    if brackets[i] == "(":
        tmp *= 2
        stack.append(brackets[i])
    elif brackets[i] == "[":
        tmp *= 3
        stack.append(brackets[i])
    elif brackets[i] == ")":
        if not stack or stack.pop() != "(":
            res = 0
            break
        if brackets[i - 1] == "(":
            res += tmp
        tmp //= 2
    elif brackets[i] == "]":
        if not stack or stack.pop() != "[":
            res = 0
            break
        if brackets[i - 1] == "[":
            res += tmp
        tmp //= 3
print(0 if stack else res)
