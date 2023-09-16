k, n = map(int, input().split())
temperature = list(map(int, input().split()))

prefix = [0 for _ in range(k + 2)]
for i in range(k):
    prefix[i + 1] = prefix[i] + temperature[i]

answer = -100 * 100000
for i in range(n, k + 1):
    answer = max(answer, prefix[i] - prefix[i - n])
print(answer)
