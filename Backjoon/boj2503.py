# 2503. 숫자 야구

from sys import stdin


def baseball(a, b):
    res1 = res2 = 0
    
    for i in range(3):
        if a[i] == b[i]: res1 += 1
        if a[i] in b: res2 += 1
        
    return res1, res2 - res1


sol = 0
input = stdin.readline
N = int(input())
games = [list(map(int, input().split())) for _ in range(N)]

for num1 in range(123, 1000):
    if '0' in str(num1) or len(set(str(num1))) != 3: continue
    for num2, strik, ball in games:
        if (strik, ball) != baseball(str(num1), str(num2)): break
    else:
        sol += 1
        
print(sol)
