t=int(input())
for _ in range(t):
    n = int(input())
    a=list(map(int,input().split()))
    max=0
    i=0
    while i<n:
        if  a[i] > a[max]:
            max=i
        i+=1
    if max==0:
        s_max=1
    else:
        s_max=0
    i=0
    while (i<n):
        if (a[i] > a[s_max]) and i!=max:
            s_max=i
        i+=1   
    print(a[max])
    print(a[s_max])
