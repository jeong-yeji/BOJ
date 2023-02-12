grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range(int(input())):
    n, k = map(int, input().split())
    scores = []
    for _ in range(n):
        mid, fin, hw = map(int, input().split())
        score = mid * 0.35 + fin * 0.45 + hw * 0.2
        scores.append(score)
    sorted_scores = sorted(scores, reverse=True)
    rank = sorted_scores.index(scores[k - 1])
    idx = rank // (n // 10)
    print(f'#{t + 1} {grade[idx]}')
