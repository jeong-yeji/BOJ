def sol1(numbers):
    import bisect

    zipped = sorted(list(set(numbers)))
    print(' '.join(str(bisect.bisect_left(zipped, number)) for number in numbers))


def sol2(numbers):
    zipped = {v: i for i, v in enumerate(sorted(set(numbers)))}
    print(' '.join(str(zipped[number]) for number in numbers))


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    sol1(numbers)
    sol2(numbers)
