# https://programmers.co.kr/learn/courses/30/lessons/76501


def solution(absolutes, signs):
    answer = 0

    for num, sign in zip(absolutes, signs):
        answer += num if sign else -num

        # if sign:
        #     answer += num
        # else:
        #     answer -= num

    return answer