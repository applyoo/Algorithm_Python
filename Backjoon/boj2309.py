# 2309. 일곱 난쟁이

def comb(arr, n):
    global flag
    
    if flag: return
    if len(arr) == 7:
        if sum(arr) == 100:
            flag = 1
            print(*sorted(arr))
        return
    
    for i in range(n, 9):
        arr.append(A[i])
        comb(arr, n+1)
        arr.pop()


A = [int(input()) for _ in range(9)]
flag = 0
comb([], 0)
