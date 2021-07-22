# 곱하기 혹은 더하기


def solution(s):
    answer = 0
    for i in s:
        i = int(i)
        if answer > 1 and i > 1:
            answer *= i
        else:
            answer += i
    return answer


print(solution("02984"))
print(solution("567"))
