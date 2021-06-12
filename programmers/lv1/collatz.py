# https://programmers.co.kr/learn/courses/30/lessons/12943


def solution(num):
    cnt = 0

    while num != 1:
        if num % 2:
            num = num * 3 + 1
        else:
            num /= 2

        cnt += 1
        if cnt == 500:
            return -1

    return cnt


print(solution(6))
print(solution(16))
print(solution(626331))