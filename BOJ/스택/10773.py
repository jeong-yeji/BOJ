# 제로
import sys

numbers = []
for _ in range(int(input())):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        numbers.pop()
    else:
        numbers.append(n)
print(sum(numbers))