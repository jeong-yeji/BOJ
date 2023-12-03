import sys

numbers = []
for _ in range(int(input())):
    n = int(sys.stdin.readline().rstrip())
    if n:
        numbers.append(n)
    else:
        numbers.pop()
print(sum(numbers))
