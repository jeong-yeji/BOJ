# https://programmers.co.kr/learn/courses/30/lessons/42584


def solution(prices):
    l = len(prices)

    answer = []
    for i in range(l):
        sec = l - (i + 1)
        for j in range(i + 1, l):
            if prices[i] > prices[j]:
                sec = j - i
                break
        answer.append(sec)

    # answer = [0] * l
    # for i in range(l):
    #     for j in range(i+1, l):
    #         answer[i] += 1
    #         if prices[i] > prices[j]:
    #             break

    return answer


print(solution([1, 2, 3, 2, 3]))