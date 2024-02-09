n = int(input())
cnt = 0
for number in map(int, input().split()):
    if number == 1:
        continue
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            break
    else:
        cnt += 1
print(cnt)
