t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    sum=0
    for i in range(l,r+1):
        if str(i)==str(i)[::-1]:
            sum+=i
    print(sum) 
