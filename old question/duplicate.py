t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    i=0
    count=0
    while i<n:
        j=1
        while j<n:
            if a[i]==a[j]:
                # print(a[i])
                count+=1
                # break
            j+=1
        i+=1
        if count==1:
            print(a[i])

