# 상수
a, b = map(str, input().split())
a = a[::-1]
b = b[::-1]
print(max(a, b))
# print(a if a > b else b)

print(max(input()[::-1].split()))