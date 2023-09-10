# 단어 공부
s = input().upper()
cnt = {}
for i in range(65, 91):
    cnt[chr(i)] = s.count(chr(i))

m = max(cnt.values())
if list(cnt.values()).count(m) > 1:
    print("?")
else:
    for k, v in cnt.items():
        if v == m:
            print(k)
            break

# reverse_dict = dict(map(reversed, dict.items()))
