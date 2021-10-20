from sys import stdin 
input = stdin.readline

K = int(input())
stack = []
for _ in range(K):
    new = int(input())
    if new != 0:
        stack.append(new)
    else:
        stack.pop()
print(sum(stack))