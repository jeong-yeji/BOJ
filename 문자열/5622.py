# 다이얼
dial = input()
sum = 0
alphabet = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
for d in dial:
    for idx, a in enumerate(alphabet):
        if d in a:
            sum += idx + 3
            break
print(sum)
