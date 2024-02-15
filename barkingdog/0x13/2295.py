import bisect
import itertools
import sys

input = lambda: sys.stdin.readline().strip()


def sol1():  # 68008kb, 292ms
    n = int(input())
    numbers = sorted(int(input()) for _ in range(n))
    two = set(i + j for i in numbers for j in numbers)
    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            if numbers[i] - numbers[j] in two:
                return numbers[i]


def sol2():  # 65940kb, 188ms
    n = int(input())
    numbers = sorted(int(input()) for _ in range(n))[::-1]
    two = {i + j for i, j in itertools.combinations_with_replacement(numbers, 2)}
    for i in numbers:
        for j in numbers:
            if i - j >= 0 and i - j in two:
                return i


def sol3():  # 70792kb, 352ms
    n = int(input())
    numbers = sorted(int(input()) for _ in range(n))
    two = sorted(set(i + j for i in numbers for j in numbers))
    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            if numbers[i] - numbers[j] == two[bisect.bisect_left(two, numbers[i] - numbers[j])]:
                return numbers[i]


if __name__ == "__main__":
    # print(sol1())
    # print(sol2())
    print(sol3())
