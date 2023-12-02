n, k = map(int, input().split())
people = list(range(1, n + 1))
idx = 0
result = []

for i in range(n):
    idx = (idx + k - 1) % len(people)
    result.append(str(people.pop(idx)))

print(f"<{(', '.join(result))}>")
