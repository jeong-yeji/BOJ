# 괄호
for _ in range(int(input())):
    bracket = input()
    balance, flag = 0, 1
    for b in bracket:
        if b == "(":
            balance += 1
        else:
            balance -= 1

        if balance < 0:
            flag = 0
            break

    print("YES" if flag and balance == 0 else "NO")
