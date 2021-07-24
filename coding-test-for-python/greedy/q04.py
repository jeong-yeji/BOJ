# 만들 수 없는 금액


from itertools import combinations


def solution(n, currency):
    currency.sort()
    target = 1
    for c in currency:
        if target < c:
            break
        target += c
    return target


print(solution(5, [3, 2, 1, 1, 9]))