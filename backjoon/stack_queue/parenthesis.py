T = int(input())

def solution():
    stack = []
    row = input()
    for i in range(len(row)):
        if row[i] == ')':
            if stack:
                stack.pop()
            else:
                return print('NO')
        else:
            stack.append(row[i])
    if stack:
        return print('NO') 
    return print('YES')

for _ in range(T):
    solution()