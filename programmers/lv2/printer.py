# https://programmers.co.kr/learn/courses/30/lessons/42587


def solution(priorities, location):
    idxlist = [False for _ in range(len(priorities))]
    idxlist[location] = True
    answer = 0

    while True:
        if priorities[0] == max(priorities):
            answer += 1

            if idxlist[0]:
                break

        else:
            priorities.append(priorities[0])
            idxlist.append(idxlist[0])

        del priorities[0]
        del idxlist[0]

    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))