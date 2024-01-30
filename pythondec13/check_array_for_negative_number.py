a=[11,2,-13,-21,3,7]
i=0
count=0
while i<len(a):
    if a[i]<=0:
        count+=1
    i+=1
if count>=1:
    print("YES")
else:
    print("NO")           