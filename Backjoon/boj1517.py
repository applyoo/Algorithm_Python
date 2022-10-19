# 1517. 버블 솔트

def mergeSort(s, e):
    global sol
    if s < e:
        m = (s+e) // 2
        mergeSort(s, m)
        mergeSort(m+1, e)
        
        a, b = s, m + 1
        tmp = []
        
        while a <= m and b <= e:
            if A[a] <= A[b]:
                tmp.append(A[a])
                a += 1
            else:
                tmp.append(A[b])
                b += 1
                sol += (m-a+1)
                
        if a <= m: tmp += A[a:m+1]
        if b <= e: tmp += A[b:e+1]
        
        for i in range(len(tmp)):
            A[s+i] = tmp[i]

    
N = int(input())
A = list(map(int, input().split()))
sol = 0

mergeSort(0, N-1)
print(sol)
