# 2851. 슈퍼 마리오

nums = [int(input()) for _ in range(10)]

for i in range(1, 10):
    nums[i] += nums[i-1]
    if nums[i] >= 100:
        if 100 - nums[i-1] >= nums[i] - 100: print(nums[i])
        else: print(nums[i-1])
        break
else:
    print(nums[-1])
