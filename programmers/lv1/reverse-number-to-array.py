# https://programmers.co.kr/learn/courses/30/lessons/12932


def solution(n):
    return list(map(int, str(n)[::-1]))
    # return list(map(int, reversed(str(n))))


print(solution(12345))