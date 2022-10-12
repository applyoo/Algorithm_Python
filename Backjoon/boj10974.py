# 10974. 모든 순열

def permutation(n):
    if n == N:
        return print(*sol)
        
    for i in nums:
        if arr[i]: continue
        sol[n] = i
        arr[i] = 1
        permutation(n+1)
        arr[i] = 0
        sol[n] = 0
        

N = int(input())
sol, arr = [0] * N, [0] * (N+1)
nums = [i for i in range(1, N+1)]

permutation(0)
