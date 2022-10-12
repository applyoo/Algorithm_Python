# 10448. 유레카 이론

## 1
from sys import stdin


input = stdin.readline
T = int(input())
sol = dict()
nums = [0]

while 1:
    if nums[-1] >= 1000:
        nums = nums[1:]
        break
    nums.append(nums[-1] + len(nums))

for i in range(len(nums)):
    for j in range(i, len(nums)):
        for k in range(j, len(nums)):
            sol[nums[i] + nums[j] + nums[k]] = 1

for _ in range(T):
    K = int(input())
    if K in sol:
        print(1)
    else: print(0)
    

## 2
# from sys import stdin


# def combination(n, arr):
#     if n == 3:
#         sol[sum(arr)] = 1
#         return
    
#     if sum(arr) >= 1000: return
    
#     for i in range(arr[n], len(nums)):
#         arr[n] = nums[i]
#         combination(n+1, arr)
#         arr[n] = 0
    
    
# input = stdin.readline
# T = int(input())
# sol = dict()
# nums = [0]

# while 1:
#     if nums[-1] >= 1000:
#         nums = nums[1:]
#         break
#     nums.append(nums[-1] + len(nums))

# combination(0, [0, 0, 0])

# for _ in range(T):
#     K = int(input())
#     if K in sol:
#         print(1)
#     else: print(0)
