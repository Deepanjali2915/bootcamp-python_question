t=int(input("Enter the number: "))
for i in range(t):
    n=int(input("Enter the len: "))
    a=list(map(int,input().split()))
    b=11
    count=0
    for i in range(n):
        if a[i]==b:
            count+=1
    if count>=1:
        print("YES")
    else:
        print("NO")            
