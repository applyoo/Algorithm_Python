# 2446. 별 찍기-9

N = int(input())

for i in range(-N+1, N):
    print('{0}{1}'.format(' '*(N-abs(i)-1), '*'*abs(2*abs(i)+1)))
