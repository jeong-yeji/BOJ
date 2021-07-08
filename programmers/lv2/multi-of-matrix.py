# https://programmers.co.kr/learn/courses/30/lessons/12949


def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr2[0])):
            sum = 0
            for k in range(len(arr2)):
                sum += arr1[i][k] * arr2[k][j]
            answer[i].append(sum)

    return answer


# 한줄로도..
# return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
# zip(*B) : 행<>열

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))