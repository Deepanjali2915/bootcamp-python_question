t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    i=0
    count=[]
    while i<n:
        j=1
        while j<n:
            if a[i]==a[j]:
                count+=a[i]
                print(coun)
            j+=1
        i+=1

