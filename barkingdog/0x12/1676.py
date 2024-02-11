def sol1(n):
    import math
    s = str(math.factorial(n))
    for i in range(1, len(s) + 1):
        if s[-i] != '0':
            return i - 1


def sol2(n):
    return n // 5 + n // 25 + n // 125


if __name__ == "__main__":
    n = int(input())
    print(sol1(n))
