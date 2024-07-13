# 1
a=[1,2,3,4,5,6,7,1,2,3,4,5,6]
i=0
count=1
# b=[]
while i<len(a)-1:
  if a[i]<=a[i+1]:
    count+=1 
    # b=b+[count]
  else:
    count=1
  i+=1 
max=0
# j=0
# while j<len(b):
if count>max:
  max=count
  # j+=1 
print(max)