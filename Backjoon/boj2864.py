# 2864. 5와 6의 차이

def change_num(flag, num):
    res = ''
    if flag:
        for i in num:
            res += '6' if i =='5' else i
    else: 
        for i in num:
            res += '5' if i =='6' else i
    return int(res)


A, B = map(list, input().split())

print(change_num(0, A)+change_num(0, B), change_num(1, A)+change_num(1, B))
