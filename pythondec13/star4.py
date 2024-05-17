n=int(input())
k=1
i=1
while i<=n:
    b=1
    while b<=n-i:
        print(" ",end="")
        b+=1
    j=1
    while j<=k:
        print("*",end="")
        j+=1
    k+=2    
    print()
    i+=1        