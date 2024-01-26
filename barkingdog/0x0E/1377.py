import sys

input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
sorted_numbers = sorted(numbers)
D = {sorted_numbers[i]: i for i in range(n)}
print(max(i - D[numbers[i]] for i in range(n)) + 1)
