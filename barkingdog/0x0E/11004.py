import sys

input = lambda: sys.stdin.readline().strip()


def quick_sort(start, end, k):
    global numbers
    if start < end:
        pivot = partition(start, end)
        if pivot == k:
            return
        elif k < pivot:
            quick_sort(start, pivot - 1, k)
        else:
            quick_sort(pivot + 1, end, k)


def partition(start, end):
    global numbers
    if start + 1 == end:
        if numbers[start] > numbers[end]:
            numbers[start], numbers[end] = numbers[end], numbers[start]
        return end

    mid = (start + end) // 2
    numbers[start], numbers[mid] = numbers[mid], numbers[start]
    pivot = numbers[start]
    left, right = start + 1, end

    while left <= right:
        while pivot < numbers[right] and right > 0:
            right -= 1
        while pivot > numbers[left] and left < len(numbers) - 1:
            left += 1
        if left <= right:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
            right -= 1

    numbers[start], numbers[right] = numbers[right], pivot
    return right


n, k = map(int, input().split())
numbers = list(map(int, input().split()))
quick_sort(0, n - 1, k - 1)
print(numbers[k - 1])
