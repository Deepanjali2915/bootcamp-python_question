t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    sum=0
    max=0
    for i in range(n):
        sum+=a[i]
        x=(sum/(i+1))
        if x>max:
            max = x
    print(max)
