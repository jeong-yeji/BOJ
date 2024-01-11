def dfs(answer, cnt):
    global plus, minus, divide, times
    if cnt == len(numbers):
        result.append(answer)
        return
    if plus > 0:
        plus -= 1
        dfs(answer + numbers[cnt], cnt + 1)
        plus += 1
    if minus > 0:
        minus -= 1
        dfs(answer - numbers[cnt], cnt + 1)
        minus += 1
    if divide > 0:
        divide -= 1
        dfs(answer * numbers[cnt], cnt + 1)
        divide += 1
    if times > 0:
        times -= 1
        dfs(int(answer / numbers[cnt]), cnt + 1)
        times += 1


n = int(input())
numbers = list(map(int, input().split()))
plus, minus, divide, times = map(int, input().split())
result = []
dfs(numbers[0], 1)
print(max(result))
print(min(result))
