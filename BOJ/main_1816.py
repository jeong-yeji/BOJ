TC = int(input())

for _ in range(TC):
  n = int(input())
  for i in range(2, 1_000_001):
    if n % i == 0:
      print("NO")
      break
  else:
    print("YES")