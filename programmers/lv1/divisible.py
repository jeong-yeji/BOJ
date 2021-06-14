# https://programmers.co.kr/learn/courses/30/lessons/12910


def solution(arr, divisor):
    answer = []
    for item in arr:
        if item % divisor == 0:
            answer.append(item)
    if len(answer) == 0:
        answer.append(-1)
    return sorted(answer)


# 한줄로도...
# return sorted([n for n in arr if n%divisor == 0]) or [-1]
# 값이 있으면 True, 없으면 False