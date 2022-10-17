# 2504. 괄호의 값

def solve(word1):
    if not stack: return 1
    word2 = '[' if word1 == ']' else '('
    while stack[-1] != word2:
        value = stack.pop()
        if not stack or type(value) != type(0): return 1
        if type(stack[-1]) == type(0): stack[-1] += value
    stack.pop()
    stack.append(value*3) if word2 == '[' else stack.append(value*2)


arr = input().replace('()', '2').replace('[]', '3')
stack = []

for i in arr:
    if i in ('(', '['): stack.append(i)
    elif i in (')', ']'):
        if solve(i):
            print(0)
            break
    else: stack.append(int(i))
else:
    try : print(sum(stack))
    except: print(0)
