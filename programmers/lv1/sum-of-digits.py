# https://programmers.co.kr/learn/courses/30/lessons/12931


def solution(n):
    # 1
    return sum([int(i) for i in str(n)])

    # 2
    # return sum(map(int, str(n)))


print(solution(123))
print(solution(987))