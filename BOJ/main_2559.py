k, n = map(int, input().split())
temperature = list(map(int, input().split()))
answer = [sum(temperature[:n])]
for i in range(n, k):
    answer.append(answer[-1] + temperature[i] - temperature[i - n])
print(max(answer))
