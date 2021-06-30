# https://programmers.co.kr/learn/courses/30/lessons/42747


# def solution(citations):
#     for h in range(max(citations), -1, -1):
#         tmp = 0
#         for c in citations:
#             if c >= h:
#                 tmp += 1

#         if h <= tmp:
#             return h


def solution(citations):
    citations.sort(reverse=True)
    return max(map(min, enumerate(citations, start=1)))


# 내림차순 정렬
# idx를 1부터 하면 idx가 나보다 많이 인용된 논문의 수
# h-index 성립하지 않을 때 : idx가 더 작음
# h-index 성립할 때 : idx가 더 크거나 같음
# => idx, value 중 더 작은 값 구함
# 이 중 가장 큰 값이 h-index

print(solution([3, 0, 6, 1, 5]))