from sys import stdin, stdout 
input = stdin.readline 
print = stdout.write 

for _ in range(5):
    print(str(int(input()) + 1) + '\n')

