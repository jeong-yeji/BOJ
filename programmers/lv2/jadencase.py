# https://programmers.co.kr/learn/courses/30/lessons/12951


def solution(s):
    s = s.lower().split(" ")
    answer = ""
    for i in s:
        if i == "":
            answer += " "
        else:
            answer += i[0].upper() + i[1:] + " "

    return answer[:-1]


print(solution("3people unFollowed me"))
print(solution("for the last week"))