# 평균
# 점수를 점수/최댓값*100으로 바꿔 계산
n = int(input())
result = list(map(int, input().split()))[:n]
m = max(result)
for i in range(n):
    result[i] = result[i] / m * 100
print(sum(result) / n)

# print(sum(result) / m * 100 / n)
# print(sum(result) / max(result) * 100 / n)
