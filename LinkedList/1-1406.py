import sys
input = sys.stdin.readline

lis = list(input().strip())
n = int(input())
stack = []

for i in range(n):
    
    command = input().split()
    if command[0] == 'P':
        lis.append(command[1])
        
    elif command[0] == 'L' and lis:
        
        a = lis.pop()
        stack.append(a)
        
    elif command[0] == 'D' and stack:
        a = stack.pop()
        lis.append(a)
        
    elif command[0] == 'B' and lis:
        lis.pop()


print(''.join(lis+stack[::-1]))
