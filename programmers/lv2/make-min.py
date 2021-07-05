# https://programmers.co.kr/learn/courses/30/lessons/12941


def solution(A, B):
    sum = 0
    A.sort()
    B.sort(reverse=True)

    # return sum([a*b for a, b in zip(A, B)])

    for a, b in zip(A, B):
        sum += a * b

    return sum


print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))