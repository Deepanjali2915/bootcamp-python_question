# b=[1, 2, 3, 4, 5]
# i=0
# while i<len(b):
#   j=0
#   while j<=i:
#     print(b[j],end="")
#     j+=1
#   print()
#   i+=1

a=[5, 11, 7, 4, 8, 11, 6, 4, 9]
max=0
item=a[0]
i=0
while i<len(a)-1:
  count=1
  j=i+1
  while j<len(a):
    if a[i]==a[j]:
      count+=1
    j+=1    
  if count>max:
    max=count
    item=a[i]
  i+=1 
print(item )