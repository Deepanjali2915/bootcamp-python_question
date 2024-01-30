# n=int(input())
# for i in range(n):
t=int(input())
a=list(map(int,input().split()))
i=0
count=0
while i<t:
    if a[i]%2==0:
        count+=1    
    i+=1
print(count)    
