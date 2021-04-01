# Fly me to the Alpha Centauri
import math, sys

for _ in range(int(input())):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x
    root = math.floor(math.sqrt(distance))
    if distance <= 3:
        print(distance)
    elif root ** 2 == distance:
        print(root * 2 - 1)
    elif root ** 2 + root < distance:
        print(root * 2 + 1)
    else:
        print(root * 2)
