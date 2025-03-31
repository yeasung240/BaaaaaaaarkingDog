# https://www.acmicpc.net/problem/10808

s = input()
for i in range(ord('a'), ord('z')+1):
  print(s.count(chr(i)), end = ' ')
  
  
