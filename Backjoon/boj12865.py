# 12865. 평범한 배낭

from sys import stdin


N, K = map(int, input().split())
DP = {0: 0}

for _ in range(N):
    W, V = map(int, input().split())
    temp = {}
    for ww, vv in DP.items():
        if (W+ww) <= K and (V+vv) > DP.get(W+ww, 0):
            temp[W+ww] = V + vv
    DP.update(temp)

print(max(DP.values()))
