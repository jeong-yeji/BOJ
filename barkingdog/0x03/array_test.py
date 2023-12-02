def insert(idx, num, arr, len):
    if idx >= len:
        arr.append(num)
    else:
        arr[idx + 1:] = arr[idx:]
        arr[idx] = num
    len += 1


def erase(idx, arr, len):
    arr[idx:] = arr[idx + 1:]
    len -= 1


def printArr(arr, len):
    print(*arr)


def insert_test():
    print("***** insert test *****")
    arr = [10, 20, 30]
    len = 3
    insert(3, 40, arr, len)
    printArr(arr, len)  # 10 20 30 40
    insert(1, 50, arr, len)
    printArr(arr, len)  # 10 50 20 30 40
    insert(0, 15, arr, len)
    printArr(arr, len)  # 15 10 50 20 30 40


def erase_test():
    print("***** erase test *****")
    arr = [10, 50, 40, 30, 70, 20]
    len = 6
    erase(4, arr, len)
    printArr(arr, len)  # 10 50 40 30 20
    erase(1, arr, len)
    printArr(arr, len)  # 10 40 30 20
    erase(3, arr, len)
    printArr(arr, len)  # 10 40 30


insert_test()
erase_test()
