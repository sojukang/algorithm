from sys import stdin 
input = stdin.readline

while True:
    sentence = input().rstrip()
    if sentence == '.':
        break 
    parenthesis = ['(', ')', '[', ']']
    stack = []
    flags = True
    for i in range(len(sentence)):
        if sentence[i] in parenthesis:
            # print(stack)
            if sentence[i] == ')':
                # print(') 발견')
                if stack and stack[-1] == '(':
                    stack.pop()
                else: 
                    flags = False
            elif sentence[i] == ']':
                # print(']발견')
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    flags = False
            else:
                stack.append(sentence[i])
    if stack or not flags:
        print('no')
    else:
        print('yes')