# bubble


def bubble1(numbers, n):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


def bubble2(numbers, n):
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


def bubble3(numbers, n):
    for i in range(1, n):
        for j in range(i, 0, -1):
            if numbers[j - 1] > numbers[j]:
                numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]


if __name__ == "__main__":
    n = int(input())
    numbers = [int(input()) for _ in range(n)]

    bubble1(numbers, n)
    # bubble2(numbers, n)
    # bubble3(numbers, n)

    for number in numbers:
        print(number)
