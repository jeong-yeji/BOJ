# 소수
m = int(input())
n = int(input())
prime_list = []
for num in range(m, n + 1):
    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break
    if isPrime and num != 1:
        prime_list.append(num)

print(-1 if not len(prime_list) else f"{sum(prime_list)}\n{prime_list[0]}")