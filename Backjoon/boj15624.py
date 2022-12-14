# 15624. 피보나치 수 7

N = int(input())
DP = [0] * (N+1)

if N > 0: DP[1] = 1

for i in range(2, N+1):
    DP[i] = (DP[i-2] + DP[i-1]) % 1000000007

print(DP[-1])
