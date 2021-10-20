# bfs 
N = int(input()) # the number of computers 
M = int(input()) # the number of lines between computers
from collections import deque  
graph = [[] for _ in range(N+1)] 
visited = [False] * (N+1)
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)  # undirected graph

# queue = deque([graph[1]])
# visited[1] = True 
# cnt = 0
# while queue:
#     node = queue.popleft()
#     for successor in node:
#         if not visited[successor]:
#             visited[successor] = True 
#             cnt += 1
#             # print(successor)
#             queue.append(graph[successor])

# print(cnt)

# dfs 
stack = [1]
cnt = -1
while stack:
    node = stack.pop()
    if not visited[node]:
        visited[node] = True 
        cnt += 1
        # print(node)
        for successor in graph[node]:
            stack.append(successor)

print(cnt)