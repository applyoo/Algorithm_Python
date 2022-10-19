# 1377. 버블 솔트

from sys import stdin


input = stdin.readline
N = int(input())
A = [int(input()) for _ in range(N)]
A_S, A_I = sorted(A), dict()

for i in range(N):
    A_I[A_S[i]] = i
    
sol = 0
for i in range(N):
    tmp = i - A_I[A[i]]
    if tmp > 0: sol = max(sol, tmp)

print(sol+1)
