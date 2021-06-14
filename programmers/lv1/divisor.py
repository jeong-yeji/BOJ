# https://programmers.co.kr/learn/courses/30/lessons/77884

# 내가 푼 방식
# def solution(left, right):
#     answer = 0

#     for num in range(left, right + 1):
#         cnt = 0
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 cnt += 1

#         answer += num if cnt % 2 == 0 else -num

#     return answer


# 약수의 개수가 홀수 => 정수의 제곱
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i
    return answer


print(solution(13, 17))
print(solution(24, 27))