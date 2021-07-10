# https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3


def solution(bridge_length, weight, truck_weights):
    queue = [0] * bridge_length
    time = 0

    while queue:
        time += 1
        queue.pop(0)

        if truck_weights:
            if sum(queue) + truck_weights[0] <= weight:
                queue.append(truck_weights.pop(0))
            else:
                queue.append(0)

    return time


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
