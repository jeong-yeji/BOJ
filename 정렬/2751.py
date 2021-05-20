# 수 정렬하기 - O(nlogn) : merge sort, heap sort, built-in sort method
def merge_sort(numlist):
    if len(numlist) < 2:
        return numlist

    mid = len(numlist) // 2
    leftArr = merge_sort(numlist[:mid])
    rightArr = merge_sort(numlist[mid:])

    mergelist = []
    l = r = 0
    while l < len(leftArr) and r < len(rightArr):
        if leftArr[l] < rightArr[r]:
            mergelist.append(leftArr[l])
            l += 1
        else:
            mergelist.append(rightArr[r])
            r += 1

    mergelist += leftArr[l:]
    mergelist += rightArr[r:]
    return mergelist


def heap_sort(numlist):
    return numlist


numlist = []
for _ in range(int(input())):
    numlist.append(int(input()))

numlist = merge_sort(numlist)
# numlist = heap_sort(numlist)
# numlist.sort()
# numlist = sorted(numlist)

for n in numlist:
    print(n)
