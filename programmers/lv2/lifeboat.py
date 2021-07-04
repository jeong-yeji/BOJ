# https://programmers.co.kr/learn/courses/30/lessons/42885


def solution(people, limit):
    people.sort()
    answer, s, e = 0, 0, len(people) - 1

    while s <= e:
        answer += 1
        if people[s] + people[e] <= limit:
            s += 1
        e -= 1

    return answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))