from sys import stdin
from collections import deque 
input = stdin.readline 

N = int(input())
queue = deque()
for _ in range(N):
    command = input()
    if command[:4] == 'push':
        queue.append(int(command[5:]))
    elif command[:3] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command[:4] == 'size':
        print(len(queue))
    elif command[:5] == 'empty':
        if not queue:
            print(1)
        else: 
            print(0)
    elif command[:5] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[:4] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        print('Unvalid command')