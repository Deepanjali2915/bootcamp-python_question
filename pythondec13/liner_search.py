a=[3,5,10,3,16,25,33]
# b=int(input())
i=0
count=0
while i<len(a)-1:
    if a[i]<a[i+1]:
        count+=1
    i+=1
print(count,len(a))
if count==len(a)-1:
    print("YES")
else:
    print("NO")                