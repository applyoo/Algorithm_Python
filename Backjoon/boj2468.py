# 2468. 안전 영역

## 1. bfs
from collections import deque


def bfs(r, c, h):
    q = deque([(r, c)])
    check[r][c] = 1
    
    while q:
        r, c = q.popleft()
        for (rn, cn) in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if (-1<rn<N) and (-1<cn<N) and check[rn][cn] == 0 and arr[rn][cn] > h:
                q.append((rn, cn))
                check[rn][cn] = 1
    return 1
    
    
sol = 1
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for h in set(sum(arr, [])):
    num = 0
    check = [[0] * N for _ in range(N)]
    
    for i in range(N**2):
        r, c = divmod(i, N)
        if check[r][c] == 0 and arr[r][c] > h: num += bfs(r, c, h)
        
    sol = max(sol, num)

print(sol)


## 2. dfs
# import sys


# def dfs(r, c):
#     check[r][c] = 1
#     for (rn, cn) in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
#         if (-1<rn<N) and (-1<cn<N) and check[rn][cn] == 0 and arr[rn][cn] > h: dfs(rn, cn)
#     return 1


# sys.setrecursionlimit(10000)
# sol = 1
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]

# for h in set(sum(arr, [])):
#     num = 0
#     check = [[0] * N for _ in range(N)]

#     for i in range(N**2):
#         r, c = divmod(i, N)
#         if check[r][c] == 0 and arr[r][c] > h: num += dfs(r, c)

#     sol = max(sol, num)

# print(sol)
