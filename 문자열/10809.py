# 알파벳 찾기
# 방법 1
s = input()
alphabet = [101] * 26
for idx, spell in enumerate(s):
    i = ord(spell) - 97
    if alphabet[i] == 101:
        alphabet[i] = idx

for a in alphabet:
    if a == 101:
        print(-1, end=" ")
    else:
        print(a, end=(" "))


# 방법 2
a = list(input())

for i in range(97, 123):
    if a.count(chr(i)) == 0:
        print(-1, end=" ")
    else:
        print(a.index(chr(i)), end=" ")
