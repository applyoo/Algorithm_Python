# 13421 국민 랜드

def permutation(res, C, visit, n, v):
    if n == 4:
        res.append(v)
        return
    for i in range(4):
        if visit[i]: continue
        v += C[n*4+i]
        visit[i] = 1
        permutation(res, C, visit, n+1, v)
        visit[i] = 0
        v -= C[n*4+i]
        
        
def solve(l):
    B = [(l,l), (-l,l), (-l,-l), (l,-l)]
    C = []
    res = []
    
    for x, y in A:
        for a, b in B:
            C.append(abs(a-x) + abs(b-y))
    
    permutation(res, C, [0,0,0,0], 0, 0)
    return min(res)


A = []
for _ in range(4):
    A.append(list(map(lambda x: int(x)*2, input().split())))

s = max(1, min(list(map(abs, sum(A, [])))))
e = max(1, max(list(map(abs, sum(A, [])))))
sol = [1e20, 1]

while s <= e:
    m1 = int(s+(e-s)/3)
    m2 = int(s+(e-s)*2/3)
    ans1, ans2 = solve(m1), solve(m2)
    
    if ans1 >= ans2:
        if sol[0] > ans2: sol = [ans2, m2]
        elif sol[0] == ans2: sol[1] = max(sol[1], m2)
        s = m1 + 1
    else:
        if sol[0] > ans1: sol = [ans1, m1]
        elif sol[0] == ans2: sol[1] = max(sol[1], m1)
        e = m2 - 1

print(sol[1])
