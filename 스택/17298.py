# 오큰수 : 오른쪽에 있으면서 그 수보다 큰 수 중 가장 왼쪽에 있는 수
# 이중 for문으로 돌리면 시간 초과 발생 => stack 이용
res = [-1 for _ in range(int(input()))]
numlist = list(map(int, input().split()))
stack = []

for i in range(len(numlist)):
    while len(stack) != 0 and numlist[stack[-1]] < numlist[i]:
        res[stack.pop()] = numlist[i]
    stack.append(i)

print(*res)
