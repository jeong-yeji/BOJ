# 베르트랑 공준
# 자연수 n에 대하여, n보다 크고 2n보다 작거나 같은 소수는 적어도 하나 존재함
# 방법 1
n = 123456 * 2
num_set = set(i for i in range(1, n + 1))
non_prime = set([1])
for i in range(2, int(n ** 0.5) + 1):
    for j in range(2, n // i + 1):
        non_prime.add(i * j)
prime_list = sorted(list(num_set - non_prime))

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for p in prime_list:
        if p > 2 * n:
            break
        elif p > n:
            cnt += 1
    print(cnt)


# 방법 2
n = 123456 * 2
non_prime = set([1])
for i in range(2, int(n ** 0.5) + 1):
    for j in range(2, n // i + 1):
        non_prime.add(i * j)

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if i not in non_prime:
            cnt += 1
    print(cnt)