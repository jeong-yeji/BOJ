import sys

input = lambda: sys.stdin.readline().strip()
print = lambda x: sys.stdout.write(x)

n, m = map(int, input().split())

# print(*sorted(sys.stdin.read().split(), key=int))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# i, j = 0, 0
# while i < n and j < m:
#     if a[i] < b[j]:
#         print(str(a[i]) + " ")
#         i += 1
#     else:
#         print(str(b[j]) + " ")
#         j += 1
#
# while i < n:
#     print(str(a[i]) + " ")
#     i += 1
#
# while j < m:
#     print(str(b[j]) + " ")
#     j += 1
