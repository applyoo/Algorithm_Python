# 25305. 커트라인

N, K = map(int, input().split())
X = sorted(list(map(int, input().split())), reverse=True)

print(X[K-1])
