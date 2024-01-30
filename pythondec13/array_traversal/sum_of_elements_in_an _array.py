# n=int(input())
# for i in range(n):
t=int(input())
a=list(map(int,input().split()))
i=0
count=0
while i<t:
    count+=a[i]
    i+=1
print(count) 