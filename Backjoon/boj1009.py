# 1009. 분산처리

from sys import stdin


def digit_rule(BASE, num):
    num *= BASE
    if num > 10: num %= 10
    
    if digit[BASE][0] == num: return
    else:
        digit[BASE].append(num)
        digit_rule(BASE, num)
    

input = stdin.readline
T = int(input())
digit = dict()

for i in range(1, 10):
    digit[i] = [i]
    digit_rule(i, i)
    
for _ in range(T):
    a, b = map(int, input().split())
    a %= 10
    if a == 0: print(10)
    else: print(digit[a][b%len(digit[a])-1])
