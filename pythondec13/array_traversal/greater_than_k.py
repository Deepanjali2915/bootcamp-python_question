a=[3,5,10,25,16,12,14]
k=34
i=0
count=0
while i<len(a):
    if a[i]>k:
        count+=1
        break
        # print(a[i])
    # else:
    #     print("No")    
    i+=1
if count==1:
    print(a[i])
else:
    print("No")        