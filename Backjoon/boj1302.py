# 1302. 베스트셀러

from sys import stdin
from collections import defaultdict


input = stdin.readline
books = defaultdict(int)

N = int(input())
for _ in range(N):
    books[input().strip()] += 1

print(sorted(books.items(), key = lambda x: (-x[1], x[0]))[0][0])
