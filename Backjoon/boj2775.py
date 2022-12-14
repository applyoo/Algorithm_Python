# 2775.  부녀회장이 될테야

from sys import stdin


input = stdin.readline
DP = [[i for i in range(1,15)] for _ in range(15)]

for i in range(1,15):
    for j in range(1,14):
        DP[i][j] = DP[i-1][j] + DP[i][j-1]

for _ in range(int(input())):
    K, N = int(input()), int(input())
    print(DP[K][N-1])
