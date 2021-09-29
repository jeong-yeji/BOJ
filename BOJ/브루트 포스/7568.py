# 덩치
n = int(input())
people = []

for _ in range(n):
    person = list(map(int, input().split()))
    people.append(person)

for i in range(n):
    cnt = 0
    weight = people[i][0]
    height = people[i][1]

    for person in people:
        if weight < person[0] and height < person[1]:
            cnt += 1

    print(cnt + 1, end=" ")

print()