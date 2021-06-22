# https://programmers.co.kr/learn/courses/30/lessons/12918


def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()
    # return s.isdigit() and len(s) in (4, 6)


print(solution("a234"))
print(solution("1234"))