def sol1():
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    m = int(input())
    for target in map(int, input().split()):
        s, e = 0, n - 1
        while s <= e:
            mid = (s + e) // 2
            if numbers[mid] < target:
                s = mid + 1
            elif numbers[mid] > target:
                e = mid - 1
            else:
                print(1)
                break
        else:
            print(0)


def sol2():
    import bisect

    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    m = int(input())
    for target in map(int, input().split()):
        i = bisect.bisect_left(numbers, target)
        print(1 if i < n and numbers[i] == target else 0)
