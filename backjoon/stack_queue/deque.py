from sys import stdin
from collections import deque 
input = stdin.readline 

N = int(input())
queue = deque()

for _ in range(N):
    command = input()
    if command[:9] == 'push_back':
        queue.append(int(command[10:]))
    elif command[:10] == 'push_front':
        queue.appendleft(int(command[11:]))
    elif command[:9] == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command[:8] == 'pop_back':
        if queue:
            print(queue.pop())
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