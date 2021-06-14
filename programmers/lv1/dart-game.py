# https://programmers.co.kr/learn/courses/30/lessons/17682


def solution(dartResult):
    bonus = {"S": 1, "D": 2, "T": 3}
    option = {"*": 2, "#": -1}

    answer = []
    n = ""

    for str in dartResult:
        if str.isdigit():
            n += str
        elif str in "SDT":
            answer.append(int(n) ** bonus[str])
            n = ""
        elif str in "*#":
            answer[-1] = answer[-1] * option[str]
            if str == "*" and len(answer) != 1:
                answer[-2] = answer[-2] * option[str]

    return sum(answer)


# 10을 다르 문자로 대체해서 for문 돌리기
# 정규 표현식 사용..


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))