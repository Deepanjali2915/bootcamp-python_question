t=int(input("Enter the number: "))
for i in range(t):
    n=int(input("Enter the len: "))
    a=list(map(int,input().split()))
    b=[0]*n
    j=0
    while j<n:
        b[j]=a[n-j-1]
        j+=1
    print(b)
    
    
    
    
    
    
        z=[0]*n
    
           z[i]=x
        m=len(z)
    for i in range(m-1):
        flag = 0
        for j in range(m-1):
            if z[j] > z[j+1]:
                tmp = z[j]
                z[j] = z[j+1]
                z[j+1] = tmp
                flag = 1
        if flag == 0:
            break
    print(z[-1])

            
