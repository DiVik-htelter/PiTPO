i,j =list(map(int, input("введите i и j через пробел^ ").split()))

def GenNum(a:int):
  if a%2==0: return a/2
  else: return a*3 + 1
  
maxLen=0
for n in range(i,j+1):
  len=1
  while n>1:
    len+=1
    n=GenNum(n)
  maxLen=max(maxLen, len)

print(i,j,maxLen)