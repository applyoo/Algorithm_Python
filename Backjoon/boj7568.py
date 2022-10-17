# 7568. 덩치

N = int(input())
ranks = [tuple(map(int, input().split())) for _ in range(N)]
sol = [0] * N

for i in range(N):
    rank = 1
    for j in range(N):
        if ranks[i][0] < ranks[j][0] and ranks[i][1] < ranks[j][1]:
            rank += 1
    sol[i] = rank
    
print(*sol)
