# https://programmers.co.kr/learn/courses/30/lessons/12922


def solution(n):
    if n % 2 == 0:
        return "수박" * (n // 2)
    return "수박" * (n // 2) + "수"


# return "수박" * (n // 2) + "수박" * (n % 2)


print(solution(3))
print(solution(4))