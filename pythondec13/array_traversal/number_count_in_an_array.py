# n=int(input())
# for i in range(n):
t=int(input())
a=list(map(int,input().split()))
b=int(input())
i=0
count=0
while i<t:
    if a[i]==b:
        count+=1
    i+=1
print(count)    
