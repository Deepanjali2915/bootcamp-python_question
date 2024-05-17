# a=[5,4,4,7,6,3,2,4,6,8,6,3,6,8,6,]
# a=[1,1,2,3,4,5,6]
# a=[1,1,1,2,2,3,3]
a=[1,2,4,6,4,1,3,4,4,2,3,6,]
i=1
count=1
store=[]
while i<len(a)-1:
    if a[i]<=a[i+1]:
        # print(a[i],end=" ")
        count+=1
    else:
        store.append(count) 
        count=1   
    i+=1
# print(a[i],end=" ")
# print(count,a[i],end=" ")         
j=0
max=0
while j<len(store):
  if store[j]>store[max]:
    max=j
  j+=1
print(store[max])