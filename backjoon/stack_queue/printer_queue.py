from sys import stdin 
from collections import deque 
input = stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    importance = deque(map(int, input().split()))
    cnt = 0
    target = importance[M]
    idx = M 
    while importance:
        max_importance = max(importance)

        if importance[0] == max_importance:
            cnt += 1
            if importance.popleft() == target and idx == 0:
                print(cnt)
                break 

        else:
            importance.rotate(-1) 
        
        if idx == 0:
            idx = len(importance) - 1
        else:
            idx -= 1
