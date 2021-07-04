# https://programmers.co.kr/learn/courses/30/lessons/12953


def get_gcd(n, m):
    n, m = max(n, m), min(n, m)

    while m:
        n, m = m, n % m

    return n


def solution(arr):
    lcm = 1
    for i in arr:
        lcm = lcm * i // get_gcd(i, lcm)
    return lcm


print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))
