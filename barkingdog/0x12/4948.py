R = 123_456 * 2 + 1
prime = [1] * R
prime[0] = prime[1] = 0
for i in range(2, R):
    if prime[i]:
        for j in range(i * i, R, i):
            prime[j] = 0
            
while True:
    n = int(input())
    if n == 0:
        break
    print(sum(prime[n + 1:2 * n + 1]))
