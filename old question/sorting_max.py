t=int(input())
for k in range(t):
    a=list(map(int,input().split()))
    n=len(a)
    i=0
    while(i<n):
        j=i
        min=j
        while (j<n):
            if a[j]<a[min]:
                min=j
            j+=1
            
        temp=a[i]
        a[i]=a[min]
        a[min]=temp
        i+=1
    print(a)   
