n, p, q = map(int, input().split())
dict = {0: 1}


def solution(n):
    if n not in dict:
        dict[n] = solution(n // p) + solution(n // q)
    return dict[n]


print(solution(n))
