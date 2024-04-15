a=[5,4,5,7,6,3,2,4,6]
i=0
count=1
max=1
while i<len(a)-1:
    if a[i]<a[i+1]:
        count+=1
    else:
        count=1
        # break
    if count>max :
        max=count

    i+=1
print(max)    