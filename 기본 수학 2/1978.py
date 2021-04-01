# 소수 찾기
# 방법 1 : cnt+=1
n = int(input())
num_list = list(map(int, input().split()))[:n]
cnt = 0
for num in num_list:
    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break
    if isPrime and num != 1:
        cnt += 1
print(cnt)


# 방법 2 : n-=1
n = int(input())
num_list = list(map(int, input().split()))[:n]
for num in num_list:
    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break
    if num == 1 or not isPrime:
        n -= 1
print(n)