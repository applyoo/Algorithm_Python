# 2864. 5와 6의 차이

def change_num(flag, num):
    ans = ''
    if flag:
        for i in num:
            ans += '6' if i =='5' else i
    else: 
        for i in num:
            ans += '5' if i =='6' else i
    return int(ans)


A, B = map(list, input().split())

print(change_num(0, A)+change_num(0, B), change_num(1, A)+change_num(1, B))
