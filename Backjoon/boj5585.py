# 5585. 거스름돈

N = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
sol = 0

for coin in coins:
    sol += N // coin
    N %= coin

print(sol)
