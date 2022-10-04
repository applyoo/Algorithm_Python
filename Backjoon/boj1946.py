# 1946. 신입 사원

from sys import stdin


input = stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    sol = 1
    score = [0] * (N+1)
    
    for i in range(N):
        a, b = map(int, input().split())
        score[a] = b
    
    base = score[1]
    
    for i in range(2, N+1):
        if base > score[i]:
            sol += 1
            base = score[i]
    print(sol)
        