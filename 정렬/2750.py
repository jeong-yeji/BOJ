# 수 정렬하기 - O(n^2) : insertion sort, bubble sort
def insertio_sort(numlist):
    for i in range(1, len(numlist)):
        for j in range(i, 0, -1):
            if numlist[j - 1] > numlist[j]:
                numlist[j - 1], numlist[j] = numlist[j], numlist[j - 1]
    return numlist


def bubble_sort(numlist):
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if numlist[j] > numlist[j + 1]:
                numlist[j], numlist[j + 1] = numlist[j + 1], numlist[j]
    return numlist


numlist = []
for _ in range(int(input())):
    numlist.append(int(input()))

numlist = insertion_sort(numlist)
numlist = bubble_sort(numlist)

for n in numlist:
    print(n)