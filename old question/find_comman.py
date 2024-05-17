# t=int(input())
# for _ in range(t):
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
#c=[0]*n
#k = 0
i=0
count=0
while i<n:
    j=0
    while j<n:
        if a[i]==b[j]:
            print(a[i],end=" ")
            count+=1
    #           k+=1
        
        j+=1
    i+=1    
#print(c)  
if count>=1:
    print(a[i],end=" ")
else:
    print("NO")    
