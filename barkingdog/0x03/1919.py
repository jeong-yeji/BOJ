alphabet1 = [0] * 26
alphabet2 = [0] * 26

for i in input():
    alphabet1[ord(i) - 97] += 1

for i in input():
    alphabet2[ord(i) - 97] += 1

res = 0
for i in range(26):
    res += abs(alphabet1[i] - alphabet2[i])
print(res)
