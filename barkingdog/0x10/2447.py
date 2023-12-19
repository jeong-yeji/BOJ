def recur(n):
    if n == 1:
        return ["*"]

    stars = recur(n // 3)
    line1 = []
    line2 = []

    print(stars)
    for star in stars:
        line1.append(star * 3)
    for star in stars:
        line2.append(star + " " * (n // 3) + star)

    return line1 + line2 + line1


n = int(input())
print("\n".join(recur(n)))
