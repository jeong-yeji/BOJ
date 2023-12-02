import sys

input = sys.stdin.readline

st1 = list(input().rstrip())
st2 = []

for _ in range(int(input())):
    cmd = input().split()

    if cmd[0] == "L":
        if st1:
            st2.append(st1.pop())
    elif cmd[0] == "D":
        if st2:
            st1.append(st2.pop())
    elif cmd[0] == "B":
        if st1:
            st1.pop()
    elif cmd[0] == "P":
        st1.append(cmd[1])

st1.extend(reversed(st2))
print(''.join(st1))

# insert는 O(N) => 시간 초과
# append, pop은 O(1)
# sys.stdin.readline 안쓰면 시간초과 남
