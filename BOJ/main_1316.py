# 그룹 단어 체커
# 그룹 단어 : 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우
# 방법 1
cnt = 0
for _ in range(int(input())):
    str = ""
    l = []
    for w in input():
        if str != w:
            l.append(str)
            str = w
    l.append(str)

    if len(l) == len(set(l)):
        cnt += 1
print(cnt)


# 방법 2
cnt = 0
for _ in range(int(input())):
    word = input()
    for idx, w in enumerate(word):
        if idx != len(word) - 1:
            if w != word[idx + 1]:
                if w in word[idx + 1 :]:
                    break
        else:
            cnt += 1
print(cnt)