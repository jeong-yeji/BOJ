# 문자열 뒤집기


def solution(s):
    zero, one = 0, 0

    if s[0] == "0":
        zero += 1
    else:
        one += 1

    for a, b in zip(s, s[1:]):
        if a != b:
            if b == "0":
                zero += 1
            else:
                one += 1

    return min(zero, one)


print(solution("0001100"))
