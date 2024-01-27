import sys

input()
print('\n'.join(map(str, sorted(map(int, sys.stdin.readlines())))))
