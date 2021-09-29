# 크로바티아 알파벳
# 방법 1
croatia = input()
croatia = croatia.replace("c=", "č")
croatia = croatia.replace("c-", "ć")
croatia = croatia.replace("dz=", "dž")
croatia = croatia.replace("d-", "đ")
croatia = croatia.replace("s=", "š")
croatia = croatia.replace("z=", "ž")

l = len(croatia)
for idx, c in enumerate(croatia):
    if c == "j" and idx != 0:
        if croatia[idx - 1] == "l" or croatia[idx - 1] == "n":
            l -= 1
    if c == "d" and idx != len(croatia) - 1:
        if croatia[idx + 1] == "ž":
            l -= 1

print(l)


# 방법 2
croatia = input()
re = ["c=", "c-", "dz=", "d-", "s=", "z=", "lj", "nj"]
for r in re:
    croatia = croatia.replace(r, "*")
print(len(croatia))