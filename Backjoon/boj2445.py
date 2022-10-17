# 2445. 별 찍기-8

N = int(input())

for i in range(-N+1, N):
    print('{0}{1}{0}'.format('*'*(N-abs(i)), ' '*((abs(i))*2)))
