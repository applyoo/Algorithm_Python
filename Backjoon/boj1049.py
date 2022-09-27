# 1049. 거미줄

from sys import stdin


input = stdin.readline
N, M = map(int, input().split())
packages, lines = [0] * M, [0] * M

for i in range(M):
    packages[i], lines[i] = map(int, input().split())

packages.sort()
lines.sort()

if packages[0] >= lines[0] * 6: print(lines[0] * N)
else: print(min(packages[0] * ((N // 6) + 1), packages[0] * (N // 6) + lines[0] * (N % 6)))
