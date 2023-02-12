from collections import Counter

for t in range(int(input())):
    tc = input()
    numbers = list(map(int, input().split()))
    cnt = Counter(numbers).most_common()
    cnt.sort(key=lambda x: (-x[1], -x[0]))
    print(f'#{tc} {cnt[0][0]}')
