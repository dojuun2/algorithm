import sys

input = sys.stdin.readline

N=int(input().strip())
stack = []

for _ in range(N):
    order = input().split()
    
    if order[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order[0] == "size":
        print(len(stack))
    elif order[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif order[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        stack.append(int(order[1]))