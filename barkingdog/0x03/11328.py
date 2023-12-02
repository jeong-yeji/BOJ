import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = input().split()

    for i in set(a):
        if a.count(i) != b.count(i):
            print("Impossible")
            break
    else:
        print("Possible")
