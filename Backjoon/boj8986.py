# 8986. 전봇대

def solve(x):
    res = 0
    for i in range(1, N):
        res += abs(i*x - A[i])
    return res


N = int(input())
A = list(map(int, input().split()))

s, e, sol = 0, A[-1], 1e15

while e >= s:
    m1 = int(s + (e-s)/3)
    m2 = int(s + (e-s)*2/3)
    ans1, ans2 = solve(m1), solve(m2)
    
    if ans1 >= ans2:
        s = m1 + 1
        sol = min(sol, ans2)
    else:
        e = m2 - 1
        sol = min(sol, ans1)

print(sol)
