import math


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return a // gcd(a, b) * b


if __name__ == "__main__":
    print(gcd(20, 12))
    print(lcm(20, 12))
    print("====")
    print(math.gcd(20, 12))
    print(math.lcm(20, 12))
