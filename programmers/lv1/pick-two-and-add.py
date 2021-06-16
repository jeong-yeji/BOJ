# https://programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations


def solution(numbers):
    return sorted(set(sum(combi) for combi in combinations(numbers, 2)))


# 가독성 제로.. ㅋㅋㅋ
# def solution(numbers):
#     s=set()
#     combination = combinations(numbers, 2)
#     for combi in combination:
#         s.add(sum(combi))
#     return sorted(s)


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
