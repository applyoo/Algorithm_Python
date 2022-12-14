# 10211. Maximum Subarray

from sys import stdin


input = stdin.readline
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    DP = [A[0]]
    
    for i in range(1, N):
        if DP[-1] > 0:
            DP += [DP[-1] + A[i]]
        else:
            DP += [A[i]]
    
    print(max(DP))
