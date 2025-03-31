# The difference between previous solving and current solving is loop of N.
# Previous solving loop starts from all alpabets but this one is only from N of word

S = input()
lis = [0] * 25
for i in S:
  lis[ord(i) - ord('a')] += 1
print(*lis)
