# https://programmers.co.kr/learn/courses/30/lessons/12930
# 공백이 여러개 있는 경우 고려!!


def solution(s):
    words = s.split(" ")
    answer = ""

    for word in words:
        if word != " ":
            for idx, w in enumerate(word):
                if idx % 2:
                    answer += w.lower()
                else:
                    answer += w.upper()
        answer += " "

    return answer[:-1]


print(solution("try hello world"))