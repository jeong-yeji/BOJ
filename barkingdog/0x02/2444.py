n = int(input())
l = n * 2 - 1

for i in range(1, n):
    print(" " * ((l // 2) - (i - 1)), end="")
    print("*" * (i * 2 - 1))

for i in range(n, -1, -1):
    print(" " * ((l // 2) - (i - 1)), end="")
    print("*" * (i * 2 - 1))
