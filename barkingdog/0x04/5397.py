for _ in range(int(input())):
    pwd, st1, st2 = list(input()), [], []
    for val in pwd:
        if val == "<":
            if st1:
                st2.append(st1.pop())
        elif val == ">":
            if st2:
                st1.append(st2.pop())
        elif val == "-":
            if st1:
                st1.pop()
        else:
            st1.append(val)

    st1.extend(reversed(st2))
    print(''.join(st1))
