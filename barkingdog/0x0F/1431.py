def sum_of_int(x):
    result = 0
    for i in x:
        if i.isdigit():
            result += int(i)
    return result


serial = [input() for _ in range(int(input()))]
serial.sort(key=lambda x: (len(x), sum_of_int(x), x))
print(*serial, sep='\n')
