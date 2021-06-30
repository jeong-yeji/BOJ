# https://programmers.co.kr/learn/courses/30/lessons/12985

import math


def solution(n, a, b):
    # return ((a-1)^(b-1)).bit_length()

    a, b = min(a, b), max(a, b)
    answer = 0

    while b % 2 != 0 or b - a != 1:
        answer += 1
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)

    return answer


print(solution(8, 4, 7))