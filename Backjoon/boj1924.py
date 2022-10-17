# 1924. 2007년

x, y = map(int, input().split())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

print(date[((y-1) + sum(month[:x-1]))%7])
