# 2748. 피보나치 수 2

N = int(input())
DP = [0, 1]

for _ in range(N-1):
    DP += [DP[-2] + DP[-1]]

print(DP[-1])
