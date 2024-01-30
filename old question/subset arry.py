t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    b=list(map(int,input().split())) 
    i=0
    count=0
    while i<=len(a):
        j=0
        while j<=len(b):
            if a[i]==b[j]:
                count+=1 
            j+=1
        i+=1 
    if count==len(b):       
        print("Yes")
    else:
        print("NO")             
