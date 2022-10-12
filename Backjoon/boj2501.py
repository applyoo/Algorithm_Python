# 2501. 약수 구하기

N, K = map(int, input().split())
nums = [i for i in range(1, int(N//2)+1) if not (N % i)] + [N]

if len(nums) < K: print(0)
else: print(nums[K-1])
