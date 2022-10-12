# 1977. 완전제곱수

M, N = int(input()), int(input())
nums = [i**2 for i in range(int(M**0.5), int(N**0.5) + 1)]

if len(nums) == 1:
    if nums[0] < M:
        print(-1)
    else:
        print(sum(nums), nums[0], sep='\n')
else:
    if nums[0] < M:
        print(sum(nums[1:]), nums[1], sep='\n')
    else:
        print(sum(nums), nums[0], sep='\n')
