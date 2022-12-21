# 2417. 정수 제곱근

N = int(input())

s, e = 0, N

while e >= s:
    m = (s+e)//2
    
    if m**2 >= N: e = m-1
    else: s = m+1

print(s)
