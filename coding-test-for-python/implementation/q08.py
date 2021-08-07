# 문자열 재정렬


def solution(s):
    a = [0]

    for i in s:
        if i.isalpha():
            a.append(i)
        else:
            a[0] += int(i)

    answer = "".join(sorted(a[1:]))
    if a[0] != 0:
        answer += str(a[0])

    return answer


print(solution("K1KA5CB7"))
print(solution("AJKDLSI412K4JSJ9D"))
