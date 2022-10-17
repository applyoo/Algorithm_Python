# 1838. 버블 정렬

N = int(input())
A = list(map(int, input().split()))
A_S, A_I = sorted(A), dict()

for i in range(N):
    A_I[A_S[i]] = i

sol = 0
for i in range(N):
    tmp = i - A_I[A[i]]
    if tmp < 0: continue
    sol = max(sol, tmp)

print(sol)
