# https://programmers.co.kr/learn/courses/30/lessons/12982


def solution(d, budget):
    d.sort()
    while sum(d) > budget:
        d.pop()
    return len(d)


# 매번 sum()이면 시간 복잡도가 O(n^2)
# sum 값 구해서 빼는 방법이 나을 듯
# def solution(d, budget):
#     d.sort()
#     s = sum(d)
#     while s > budget:
#         s -= d.pop()
#     return len(d)

print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))