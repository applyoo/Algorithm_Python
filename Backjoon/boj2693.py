# 2693. N번째 큰 수

from sys import stdin


T = int(input())
sol = []

for _ in range(T):
    sol.append(sorted(list(map(int, input().split())))[-3])

print(*sol, sep='\n')
