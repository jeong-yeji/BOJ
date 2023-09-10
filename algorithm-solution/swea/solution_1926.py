for i in range(1, int(input()) + 1):
    target = str(i)
    
    cnt = 0
    cnt += target.count('3')
    cnt += target.count('6')
    cnt += target.count('9')

    if cnt:
        print('-' * cnt, end=' ')
    else:
        print(target, end=' ')
