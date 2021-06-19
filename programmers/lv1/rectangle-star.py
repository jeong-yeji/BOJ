# https://programmers.co.kr/learn/courses/30/lessons/12969

a, b = map(int, input().strip().split(" "))

# 1
# for _ in range(b):
#     for _ in range(a):
#         print("*", end="")
#     print()

# 2
print(("*" * a + "\n") * b)
