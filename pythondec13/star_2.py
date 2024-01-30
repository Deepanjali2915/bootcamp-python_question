n=int(input())
i=0
while i<n:
    j=n
    while j>i:
        print(" ", end=" ")
        j-=1
    print("*",end="")
    print()
    i+=1    
