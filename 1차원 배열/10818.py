# 최소, 최대
n = int(input())
list = list(map(int, input().split()))
list = list[:n]
print(min(list), max(list))