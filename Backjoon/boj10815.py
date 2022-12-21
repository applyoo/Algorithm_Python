# 10815. 숫자 카드

### 풀이1. 이분탐색
def binarySearch(x, s, e):
    while e >= s:
        m = (s+e)//2
        
        if x == A[m]: return 1
        elif x < A[m]: e = m - 1
        else: s = m + 1
    return 0
    
    
N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))

sol = []
for num in B:
    sol.append(binarySearch(num, 0, N-1))

print(*sol)


### 풀이2. 자료구조
# int(input())
# A = set(input().split())
# int(input())

# print(' '.join(['1' if i in A else '0' for i in input().split()]))
