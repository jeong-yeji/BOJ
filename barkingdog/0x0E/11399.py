n = int(input())
p = list(map(int, input().split()))

p.sort()

# insertion sort
# for i in range(1, n):
#     point = i
#     value = p[i]
#     for j in range(i - 1, -1, -1):
#         if p[j] < p[i]:
#             point = j + 1
#             break
#         if j == 0:
#             point = 0
#     for j in range(i, point, -1):
#         p[j] = p[j - 1]
#     p[point] = value

# 부분 합 구하기
for i in range(1, n):
    p[i] += p[i - 1]

print(sum(p))
