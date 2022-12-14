# 24416. 알고리즘 수업

N = int(input())
DP = [0, 1, 1]

for i in range(N-2):
    DP += [DP[-2] + DP[-1]]

print(DP[-1], N-2)
