# 2110. 공유기 설치

from sys import stdin


def assign(x, cnt):
    a = A[0]
    for i in range(1, N):
        if A[i] - a < x: continue
        cnt -= 1
        a = A[i]
        if not cnt: return 1
    return 0

    
def binarySearch(s, e):
    while e >= s:
        m = (s+e)//2
        
        if assign(m, C-1): s = m+1
        else: e = m-1
    return e
    

input = stdin.readline
N, C = map(int, input().split())

A = sorted([int(input()) for _ in range(N)])

print(binarySearch(0, (A[-1]-A[0])//(C-1)+1))
