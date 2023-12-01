n = int(input())

for i in range(1, n):
    print(("*" * i).ljust(n), end="")
    print(("*" * i).rjust(n))

for i in range(n, -1, -1):
    print(("*" * i).ljust(n), end="")
    print(("*" * i).rjust(n))
