a=input()
i=0
count=0
while i<len(a):
    j=i
    while j<len(a):
        if a[i]==a[j]:
            count+=1
        else:
            break
        j+=1
    print(str(count)+a[i],end='')
    count=0
    i=j   
        
            
