# 럭키 스트레이트


def solution(n):
    a = list(map(int, n[: len(n) // 2]))
    b = list(map(int, n[len(n) // 2 :]))

    if sum(a) == sum(b):
        return "LUCKY"

    return "READY"


print(solution("123402"))
print(solution("7755"))
