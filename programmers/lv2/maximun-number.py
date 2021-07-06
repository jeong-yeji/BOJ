# https://programmers.co.kr/learn/courses/30/lessons/42746


def solution(numbers):
    numbers = list(map(str, numbers))
    # numbers.sort(reverse=True, key=lambda x:(x[0], x[1%len(x)], x[2%len(x)], x[3%len(x)]))
    numbers.sort(reverse=True, key=lambda x: x * 3)
    return str(int("".join(numbers)))  # 000 처리하려고 join > int > str


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))