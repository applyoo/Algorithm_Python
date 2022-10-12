# 11497. 통나무 건너뛰기

from sys import stdin


input = stdin.readline
T = int(input())
sol = []

for _ in range(T):
    N = int(input())
    L = sorted(list(map(int, input().split())))
    L_S = [0] * N
    
    for i in range(N):
        if i % 2: L_S[N-(i//2+1)] = L[i]
        else: L_S[i//2] = L[i]
    
    diff = L_S[-1] - L_S[0]
    
    for i in range(1, N):
        diff = max(diff, abs(L_S[i] - L_S[i-1]))
    sol.append(diff)
    
print(*sol, sep='\n')
