res = [['+' for _ in range(5)] for _ in range(5)]
for i in range(5):
    res[i][i] = '#'

for i in res:
    print(''.join(i))
