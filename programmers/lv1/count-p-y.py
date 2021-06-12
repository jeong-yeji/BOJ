# https://programmers.co.kr/learn/courses/30/lessons/12916


def solution(s):
    s = s.lower()
    return s.count("p") == s.count("y")


print(solution("pPoooyY"))
print(solution("Pyy"))