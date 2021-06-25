# https://programmers.co.kr/learn/courses/30/lessons/70129


def solution(s):
    cnt, zero = 0, 0

    while s != "1":
        cnt += 1
        c = s.count("1")
        zero += len(s) - c
        s = bin(c)[2:]

    return [cnt, zero]


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
