t=int(input())
for i in range(t):
    n=int(input())
    # a,b=list(map(str,input().split()))/
    a=str(input())
    b=str(input())
    x=0
    y=0
    for i in range(n):
        if a[i]=="R" and b[i]=="S" or a[i]=="S" and b[i]=="P" or a[i]=="P" and b[i]=="R":
            x+=1 
        else:
            y+=1 
            
    if x==0:
        print(y-1)
    elif x<y :
        print(y-x)
    else:
        print(0)
