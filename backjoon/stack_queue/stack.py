from sys import stdin
input = stdin.readline 

N = int(input())
stack = [] 
for _ in range(N):
    command = input()
    if command[:4] == 'push':
        stack.append(int(command[5:]))
    elif command[:3] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[:4] == 'size':
        print(len(stack))
    elif command[:5] == 'empty':
        if not stack:
            print(1)
        else: 
            print(0)
    elif command[:3] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        print('Unvalid command')
