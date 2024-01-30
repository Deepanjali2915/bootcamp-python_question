m,n=map(int,input().split())
if n>m:
    # print("YES")
    i=0
    # count=0
    while i<n:
        if n%i==0 and m%i==0:
            print(i)
        i+=1    

else:
    print("NO")    