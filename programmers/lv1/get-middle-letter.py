# https://programmers.co.kr/learn/courses/30/lessons/12903


def solution(s):
    l = len(s) // 2
    return s[l - 1 : l + 1] if len(s) % 2 == 0 else s[l]


# 다른 풀이 : if문 안쓰고
def solution(s):
    return str[(len(s) - 1) // 2 : len(s) // 2 + 1]


print(solution("abcde"))
print(solution("qwer"))