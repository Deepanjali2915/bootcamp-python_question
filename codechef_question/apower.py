B=int(input())
i=1
x=0
while i**i<=(B):
  A=i**i
  if A==B:
    x=i 
    break 
  i+=1
if x==i:  
    print(i)
else:
    print(-1)  
# 
