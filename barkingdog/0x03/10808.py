result = [0] * 26

s = input()
for i in s:
    result[ord(i) - 97] += 1

print(*result)
