# 2512. 예산

### 풀이1. 이분탐색
def binarySearch(s, e):
    while e >= s:
        a = 0
        m = (s+e)//2
        
        for num in A:
            if m >= num: a+= num
            else: a += m
        if M >= a: s = m+1
        else: e = m-1
    return e
    
    
N = int(input())
A = list(map(int, input().split()))
M = int(input())

print(binarySearch(0, max(A)))


### 풀이2. 구현
# N = int(input())
# A = sorted(list(map(int, input().split())), reverse=True)
# M = int(input())

# a = sum(A)

# if M >= a:
#     print(A[0])
# else:
#     num = 0
#     for i in range(1, N):
#         num += (A[i-1] - A[i]) * i
#         if M >= a - num:
#             print(A[i] + int((M - (a-num))/i))
#             break
#     else:
#         print(int(M / N))
