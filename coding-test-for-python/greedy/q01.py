# 모험가 길드


def solution(n, people):
    people.sort()
    answer, cnt = 0, 0

    for p in people:
        cnt += 1
        if cnt >= p:
            answer += 1
            cnt = 0

    return answer


print(solution(5, [2, 3, 1, 2, 2]))