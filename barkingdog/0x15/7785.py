import sys

work = {}
for _ in range(int(input())):
    a, b = sys.stdin.readline().split()
    if b == "enter":
        work[a] = 1
    elif b == "leave":
        del work[a]
print('\n'.join(sorted(work.keys(), reverse=True)))
