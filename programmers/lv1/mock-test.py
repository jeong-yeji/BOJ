# https://programmers.co.kr/learn/courses/30/lessons/42840


def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer_dict = {1: 0, 2: 0, 3: 0}

    for idx, answer in enumerate(answers):
        if p1[idx % 5] == answer:
            answer_dict[1] += 1
        if p2[idx % 8] == answer:
            answer_dict[2] += 1
        if p3[idx % 10] == answer:
            answer_dict[3] += 1

    m = max(answer_dict.values())
    answer = []
    for i in range(1, 4):
        if answer_dict[i] == m:
            answer.append(i)

    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
