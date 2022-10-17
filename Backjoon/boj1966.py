# 1966. 프린터 큐

from sys import stdin
from collections import deque


input = stdin.readline
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    ranks = list(map(int, input().split()))
    arr = deque((num, i) for i, num in enumerate(ranks))
    ranks.sort(reverse=True)
    
    sol = 0
    for rank in ranks:
        while rank != arr[0][0]:
            arr.append(arr.popleft())
        sol += 1
        
        if arr[0][1] == M: break
        arr.popleft()
        
    print(sol)
    