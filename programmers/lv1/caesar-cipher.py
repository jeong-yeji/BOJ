# https://programmers.co.kr/learn/courses/30/lessons/12926


def solution(s, n):
    answer = ""

    for i in s:
        ascii = ord(i)

        if ascii > 96:
            ascii += n
            if ascii > 122:
                ascii -= 26

        elif ascii > 64:
            ascii += n
            if ascii > 90:
                ascii -= 26

        answer += chr(ascii)

    return answer


print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))