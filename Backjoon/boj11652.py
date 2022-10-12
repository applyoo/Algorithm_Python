# 11652. 카드

from sys import stdin
from collections import defaultdict


input = stdin.readline
nums = defaultdict(int)

N = int(input())
for _ in range(N):
    nums[int(input())] += 1

print(sorted(nums.items(), key = lambda x: (-x[1], x[0]))[0][0])
