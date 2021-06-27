# https://programmers.co.kr/learn/courses/30/lessons/42586

import math


def solution(progresses, speeds):
    answer = []
    works = []

    for progress, speed in zip(progresses, speeds):
        works.append(math.ceil((100 - progress) / speed))

    time, distribute = 0, 0

    for work in works:
        if time < work:
            answer.append(distribute)
            time = work
            distribute = 1
        else:
            distribute += 1
    answer.append(distribute)

    return answer[1:]


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
