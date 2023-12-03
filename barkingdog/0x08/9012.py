import sys


def isVps(bracket):
    if bracket.count("(") != bracket.count(")"):
        return False

    stack = []
    for b in bracket:
        if b == "(":
            stack.append(b)
        else:
            if stack:
                stack.pop()
            else:
                return False

    return True


for _ in range(int(input())):
    bracket = sys.stdin.readline().rstrip()
    vps = isVps(bracket)
    print("YES" if vps else "NO")
