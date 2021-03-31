# 벌집
# 방법 1
n = int(input())
sum = 2
cnt = 1

while n >= sum:
    sum += 6 * cnt
    cnt += 1

print(cnt)


# 방법 2
n = int(input()) - 2
cnt = 1

while n >= 0:
    n -= 6 * cnt
    cnt += 1

print(cnt)