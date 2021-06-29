# https://programmers.co.kr/learn/courses/30/lessons/77885


def solution(numbers):
    answer = []

    for number in numbers:
        b = bin(number)[2:]

        if number % 2 == 0:
            b = b[:-1] + "1"
        else:
            b = "0" + b
            idx = b.rfind("0")
            b = b[:idx] + "10" + b[idx + 2 :]

        answer.append(int(b, 2))

    return answer


print(solution([2, 7]))
