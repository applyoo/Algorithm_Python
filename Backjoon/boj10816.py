# 10816. 숫자 카드2

from collections import defaultdict


int(input())
A = defaultdict(int)

for i in input().split():
    A[i] += 1

int(input())

sol = [A[i] for i in input().split()]

print(*sol)
