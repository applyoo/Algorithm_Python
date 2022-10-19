# 1028. 다이아몬드 광산

def solve(flag, x, y, xn, yn):
    if dp[x][y][flag]: return
    else:
        tmp = []
        while x < R and (-1<y<C) and arr[x][y] == '1':
            tmp.append((x, y))
            x += xn
            y += yn
        
        for x, y in tmp:
            dp[x][y][flag] = len(tmp)
            

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
dp = [[[0, 0] for _ in range(C)] for _ in range(R)]

for i in range(R*C):
    r, c = divmod(i, C)
    if arr[r][c] == 0: continue
    solve(0, r, c, 1, 1)
    solve(1, r, c, 1, -1)
    

print(*dp, sep='\n')

# [0,0,0,0] [1,1,1,1] [0,0,0,0] [0,0,0,0] [0,0,0,0]
# [0,0,0,0] [0,0,0,0] [0,0,0,0] [0,0,0,0] [0,0,0,0]
# [0,0,0,0] [0,0,0,0] [0,0,0,0] [0,0,0,0] [0,0,0,0]
# [0,0,0,0] [0,0,0,0] [0,0,0,0] [0,0,0,0] [0,0,0,0]
# [0,0,0,0] [0,0,0,0] [0,0,0,0] [0,0,0,0] [0,0,0,0]


# [0, 0] [1, 1] [3, 3] [0, 0] [0, 0]
# [0, 0] [4, 3] [0, 0] [3, 4] [1, 4]
# [3, 3] [3, 1] [4, 4] [2, 4] [3, 3]
# [0, 0] [3, 4] [3, 4] [4, 3] [2, 2]
# [1, 4] [1, 4] [3, 3] [3, 2] [4, 1]
