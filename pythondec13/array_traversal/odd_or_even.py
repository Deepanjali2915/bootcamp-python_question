# n=int(input())
# for i in range(n):
t=int(input())
a=list(map(int,input().split()))
i=0
while i<t:
    if a[i]%2==0:
        print("even")
    else:
        print("Odd")    
    i+=1
