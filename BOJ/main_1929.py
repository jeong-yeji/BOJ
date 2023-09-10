# 소수 구하기
# 에라토스테네스의 체
m, n = map(int, input().split())
num_set = set(i for i in range(m, n + 1))
non_prime = set([1])
for i in range(2, int(n ** 0.5) + 1):
    for j in range(2, n // i + 1):
        non_prime.add(i * j)
for n in sorted(list(num_set - non_prime)):
    print(n)