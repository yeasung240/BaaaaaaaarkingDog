# Time complexity (n**2)

def func2(A, B):
  for i in range(0, B-1):
    for j in range(i+1, B):
      if func2[i] + func2[j] == 100:
        return 1
  return 0
  print(func2([1,52,48],3))


# Time complexity (n)

def func2(A, B):
  lis = [0] * 1001
  for i in A:
    lis[i] = 1
    if lis[100-i] == 1:
      return 1
  return 0
  
print(func2([1,52,48],3))

    
