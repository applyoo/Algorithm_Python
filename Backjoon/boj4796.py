# 4796. 캠핑

from sys import stdin


input = stdin.readline
num = 0

while 1:
    L, P, V = map(int, input().split())
    if L == 0: break
    num += 1
    print("Case {0}: {1}".format(num,(V // P) * L + min(L, V % P)))
