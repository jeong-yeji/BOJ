# https://programmers.co.kr/learn/courses/30/lessons/12934


def solution(n):
    if int(n ** 0.5) == n ** 0.5:
        return (int(n ** 0.5) + 1) ** 2
    return -1


print(solution(121))
print(solution(3))