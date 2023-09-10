for t in range(int(input())):
    encoded_str = input()

    # 문자 -> 숫자
    value_to_number = []
    for i in encoded_str:
        if i.isupper():
            value_to_number.append(ord(i) - 65)
        elif i.islower():
            value_to_number.append(ord(i) - 71)
        elif i.isdigit():
            value_to_number.append(ord(i) + 4)
        elif i == '+':
            value_to_number.append(43)
        elif i == '-':
            value_to_number.append(47)

    # 숫자 -> 2진수 6자리
    bin_numbers_2 = []
    for number in value_to_number:
        bin_numbers_2.append(format(number, 'b').zfill(6))

    # 전체 숫자 연결
    bin_numbers_str = ''.join(bin_numbers_2)

    # 8개씩 끊기
    bin_number_8 = []
    for i in range(0, len(bin_numbers_str), 8):
        bin_number_8.append(bin_numbers_str[i:i + 8])

    # 끊은 숫자들 10진수로
    numbers = []
    for number in bin_number_8:
        numbers.append(int(number, 2))

    # 10진수 -> ascii
    res = ''
    for number in numbers:
        res += chr(number)

    print(f'#{t + 1} {res}')
