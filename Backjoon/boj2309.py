# 2309. 일곱 난쟁이

## 1
def combination(arr, n):
    global flag
    
    if flag: return
    if len(arr) == 7:
        if sum(arr) == 100:
            flag = 1
            print(*sorted(arr))
        return
    
    for i in range(n, 9):
        arr.append(A[i])
        combination(arr, n+1)
        arr.pop()


A = [int(input()) for _ in range(9)]
flag = 0
combination([], 0)


## 2
# A = [int(input()) for _ in range(9)]
# A_sum = sum(A)

# for i in A:
#     for j in A:
#         if i == j: continue
#         if A_sum - (i+j) == 100:
#             A.remove(i)
#             A.remove(j)
#             print(*sorted(A), sep='\n')
#             break
#     if len(A) == 7:
#         break
