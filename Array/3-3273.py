# Two pointer

# 3273 
n = int(input())
lis = list(map(int, input().split()))
lis.sort()
a = int(input())

i = 0
j = n-1
ans = 0

while i < j:
    if lis[i] + lis[j] == a:
        j -= 1
        ans += 1 
    elif lis[i] + lis[j] > a:
        j -= 1
    elif lis[i] + lis[j] < a:
        i += 1
        
print(ans)



# Array
# 3273 
n = int(input())
lis = list(map(int, input().split()))
a = int(input())
arr = [0] * 2000001
cnt = 0 

for i in lis:
    if arr[a-i]:
        cnt += 1 
    arr[i] = 1
    
print(cnt)
