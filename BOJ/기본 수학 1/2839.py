# 설탕 배달
# 방법 1
n = int(input())
cnt = 0
while n > 0:
    if n % 5 == 0:
        cnt += n // 5
        n = 0
        break
    n -= 3
    cnt += 1
print(cnt if n == 0 else -1)


# 방법 2
n = int(input())
cnt = 0
while n > 0 and n % 5 != 0:
    n -= 3
    cnt += 1
print(-1 if n < 0 else n // 5 + cnt)
