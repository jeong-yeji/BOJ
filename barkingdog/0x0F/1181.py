import sys

words = list(set([sys.stdin.readline().strip() for _ in range(int(input()))]))
words.sort(key=len)
print(*words, sep='\n')
