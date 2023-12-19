def recur(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]
    n //= 2
    trees = recur(n)
    a = [" " * n + tree + " " * n for tree in trees]
    b = [tree + " " + tree for tree in trees]
    return a + b


print("\n".join(recur(int(input()))))
