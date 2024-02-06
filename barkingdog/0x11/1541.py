res = [sum(map(int, i.split('+'))) for i in input().split('-')]
print(res[0] - sum(res[1:]))
