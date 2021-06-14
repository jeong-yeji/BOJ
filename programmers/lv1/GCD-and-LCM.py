def solution(n, m):
    a, b = max(n, m), min(n, m)

    while b:  # b != 0:
        a, b = b, a % b

    return [a, n * m / a]


def solution(n, m):
    gcd = lambda a, b: b if not a % b else gcd(b, a % b)
    lcm = lambda a, b: a * b // gcd(a, b)
    return [gcd(n, m), lcm(n, m)]


# 참고
# https://codepractice.tistory.com/65
# https://lsjsj92.tistory.com/475