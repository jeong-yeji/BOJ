n = int(input())
cards = set(input().split())
m = int(input())
for i in input().split():
    print(int(i in cards), end=' ')
