# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        answer += 1

        if len(scoville) == 1:
            return -1

        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        new = min1 + min2 * 2
        heapq.heappush(scoville, new)

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 2, 3], 11))
print(solution([0, 0, 0, 0], 3))
