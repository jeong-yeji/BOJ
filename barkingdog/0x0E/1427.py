# print(''.join(sorted(list(input()), reverse=True)))

# selection sort

numbers = list(input())
for i in range(len(numbers)):
    tmp = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] > numbers[tmp]:
            tmp = j
    if numbers[i] < numbers[tmp]:
        numbers[i], numbers[tmp] = numbers[tmp], numbers[i]
print(''.join(numbers))
