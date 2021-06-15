# https://programmers.co.kr/learn/courses/30/lessons/12950

# 1: arr1에 바로 arr2 더하기
# def solution(arr1, arr2):
#     for i in range(len(arr1)):
#         for j in range(len(arr1[0])):
#             arr1[i][j] += arr2[i][j]
#     return arr1

# 2
# def solution(arr1, arr2):
#     answer = []
#     for i in range(len(arr1)):
#         ans = []
#         for j in range(len(arr1[0])):
#             ans.append(arr1[i][j] + arr2[i][j])
#         answer.append(ans)
#         print(answer)
#     return answer

# 3
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr1[0])):
            answer[i].append(arr1[i][j] + arr2[i][j])
    return answer


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
print(solution([[1], [2]], [[3], [4]]))
