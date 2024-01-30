t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    max1=a[0]
    max2=a[0]
    for j in range(n):
        if a[j]>max1:
            max1=a[j]
        elif a[j]>max2 and a[j]<max1:
            max2=a[j]
    print(max1,max2)        




