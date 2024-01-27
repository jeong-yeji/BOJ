import sys

input = lambda: sys.stdin.readline().strip()
print = lambda x: sys.stdout.write(x)


def merge_sort(start, end):
    if end - start < 1:
        return

    mid = (start + end) // 2

    merge_sort(start, mid)
    merge_sort(mid + 1, end)

    tmp[start:end + 1] = numbers[start:end + 1]
    k = start
    index1, index2 = start, mid + 1
    while index1 <= mid and index2 <= end:
        if tmp[index1] < tmp[index2]:
            numbers[k] = tmp[index1]
            k += 1
            index1 += 1
        else:
            numbers[k] = tmp[index2]
            k += 1
            index2 += 1

    while index1 <= mid:
        numbers[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= end:
        numbers[k] = tmp[index2]
        k += 1
        index2 += 1


n = int(input())
numbers = list(int(input()) for _ in range(n))
tmp = [0] * n
merge_sort(0, n - 1)
for number in numbers:
    print(f'{str(number)}\n')
