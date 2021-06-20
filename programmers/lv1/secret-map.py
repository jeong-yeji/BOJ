# https://programmers.co.kr/learn/courses/30/lessons/17681


def solution(n, arr1, arr2):
    answer = []

    for a, b in zip(arr1, arr2):
        a = "{0:b}".format(a).zfill(n)
        b = "{0:b}".format(b).zfill(n)

        str = ""
        for j in range(n):
            if int(a[j]) or int(b[j]):
                str += "#"
            else:
                str += " "
        answer.append(str)

    return answer


# or 연산 후 2진법으로 변환해도 같은 결과
# for i,j in zip(arr1,arr2):
#     a12 = str(bin(i|j)[2:])
#     a12=a12.rjust(n,'0')
#     a12=a12.replace('1','#')
#     a12=a12.replace('0',' ')
#     answer.append(a12)

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
