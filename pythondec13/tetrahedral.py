N=int(input())
i=0
while i<=N:
    j=0
    while j<=N:
        k=0
        while k<=N:
            if i+j+k<=3:
                print(i,j,k)
            k+=1
        j+=1
    i+=1