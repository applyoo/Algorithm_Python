# 5576. 콘테스트

from sys import stdin


input = stdin.readline
W = sorted([int(input()) for _ in range(10)])
K = sorted([int(input()) for _ in range(10)])

print(sum(W[7:]), sum(K[7:]))
